import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date, datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_portfolio = db.execute("SELECT * FROM portfolio WHERE user_id = ?", session["user_id"])
    symbols = []
    shares = []
    names = []
    prices = []
    totals = []
    total_prices = 0
    rows = len(user_portfolio)

    for row in range(rows):
        symbol = user_portfolio[row]["symbol"]
        symbols.insert(1, symbol)
        share = user_portfolio[row]["shares"]
        shares.insert(1, share)
        name = user_portfolio[row]["name"]
        names.insert(1, name)
        response = lookup(symbol)
        price = response["price"]
        usd(price)
        prices.insert(1, price)
        total = price * share
        usd(total)
        totals.insert(1, total)
        total_prices += total
        usd(total_prices)

    user_info = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    cash = user_info[0]["cash"]
    gtotal = total_prices + cash
    usd(gtotal)

    return render_template("index.html", symbols=symbols, shares=shares, names=names, prices=prices, totals=totals, cash=cash, gtotal=gtotal, rows=rows)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # If the request is GET...
    if request.method == "GET":
        return render_template("buy.html")

    # Else if the request is POST
    else:

        # If no symbol is typed in, return apology
        if not request.form.get("symbol"):
            return apology("missing symbol", 400)

        # Else if no shares typed in, return apology
        elif not request.form.get("shares"):
            return apology("missing shares", 400)

        elif not request.form.get("shares").isdigit():
           return apology("number of shares must be an integer", 400)

        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("invalid symbol", 400)

        # Get the values typed in
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        user_info = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        money = int(user_info[0]["cash"])

        # Else if the user have not enough money to buy that amount of shares
        if money < lookup(symbol)["price"] * shares:
            return apology("not enough money", 400)

        # Else (the conditions are met)
        else:
            # Get the date info
            today = date.today()

            # Store it as mm/dd/yy
            action_date = today.strftime("%m/%d/%Y")

            # Get the time info
            time = datetime.now()

            # Store it as hour:minute:second
            action_time = time.strftime("%H:%M:%S")

            # Get symbol's information
            response = lookup(symbol)

            # Calculate the amount spent
            amount = response["price"] * int(shares)

            # Record the whole action into the transactions table
            record_action = db.execute("INSERT INTO transactions (user_id, action_type, money, shares_amount, symbol, date, time) VALUES (?, 'buy', ?, ?, ?, ?, ?)",
                                       user_info[0]["id"], amount, shares, response["symbol"], action_date, action_time)

            # Update the money user have
            update_user_money = db.execute("UPDATE users SET cash = ? WHERE id = ?",
                                           user_info[0]["cash"] - amount, user_info[0]["id"])

            # Get user's portfolio to add the transaction or update the portfolio
            user_portfolio = db.execute("SELECT * FROM portfolio WHERE user_id = ?", session["user_id"])

            # Check portfolio
            if len(user_portfolio) > 1:
                check_symbol = db.execute("SELECT * FROM portfolio WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
                if len(check_symbol) > 0:
                    update_portfolio = db.execute("UPDATE portfolio SET shares = ? WHERE symbol = ?",
                                                  check_symbol[0]["shares"]+shares, symbol)
            else:
                add_portfolio = db.execute("INSERT INTO portfolio (user_id, symbol, name, shares) VALUES (?, ?, ?, ?)",
                                           user_info[0]["id"], response["symbol"], response["name"], shares)

            # Let the user know the process is completed
            flash("Transaction Completed!")

            return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_history = db.execute("SELECT * FROM transactions WHERE user_id = ?", session["user_id"])
    actions = []
    money = []
    shares = []
    symbols = []
    dates = []
    times = []
    rows = len(user_history)

    for row in range(rows):
        action = user_history[row]["action_type"]
        actions.insert(row, action)
        amount = user_history[row]["money"]
        money.insert(row, amount)
        share = user_history[row]["shares_amount"]
        shares.insert(row, share)
        symbol = user_history[row]["symbol"]
        symbols.insert(row, symbol)
        date = user_history[row]["date"]
        dates.insert(row, date)
        time = user_history[row]["time"]
        times.insert(row, time)

    return render_template("history.html", actions=actions, money=money, shares=shares, symbols=symbols, dates=dates, times=times, rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # If request is get, display form to request a stock quote
    if request.method == "GET":
        return render_template("quote.html")

    # If request is post...
    else:
        # Get the symbol input
        symbol = request.form.get("symbol")

        # Check with lookup function, if the result is None, prompt apology
        if not lookup(symbol):
            return apology("invalid symbol!", 400)

        else:
            # Get the response from lookup function
            response = lookup(symbol)

            # Return quoted.html with corresponding response
            return render_template("quoted.html", name=response["name"], symbol=response["symbol"], price=response["price"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # If the method is get, render the page
    if request.method == "GET":
        return render_template("register.html")

    # If the method is post, create the user with given information
    else:

        # Get the username
        username = request.form.get("username")

        # Get the SQL results from the db where username in table is the same as the given username.
        # If there is a row, it can be used in checking the username
        username_check = db.execute("SELECT username FROM users WHERE username = ?", username)

        # Get the password
        password = request.form.get("password")

        # Get the second password for to check
        confirmation = request.form.get("confirmation")

        # If username is not written
        if not username:
            return apology("please enter a username", 400)

        # If the username exist, then the username_check have values within
        elif len(username_check) > 0:
            return apology("the username is already exist", 400)

        elif not password or not confirmation:
            return apology("please provide the password(s)", 400)

        # Compare passwords
        elif password != confirmation:
            return apology("the passwords don't match", 400)

        # If there are no errors...
        else:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
            row = db.execute("SELECT * FROM users WHERE username = ?", username)
            session["user_id"] = row[0]["id"]
            flash('Registered!')
            return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    user_portfolio = db.execute("SELECT * FROM portfolio WHERE user_id = ?", session["user_id"])
    symbols = []
    shares = []

    for row in range(len(user_portfolio)):
        symbol = user_portfolio[row]["symbol"]
        symbols.insert(1, symbol)
        share = user_portfolio[row]["shares"]
        shares.insert(1, share)

    rows = len(symbols)

    if request.method == "GET":
        return render_template("sell.html", rows=rows, symbols=symbols)

    else:

        if not request.form.get("symbol"):
            return apology("invalid symbol", 403)

        if not request.form.get("shares"):
            return apology("invalid shares", 400)

        sell_portfolio = db.execute("SELECT * FROM portfolio WHERE user_id = ? AND symbol = ?",
                                    session["user_id"], request.form.get("symbol"))

        if int(request.form.get("shares")) > sell_portfolio[0]["shares"]:
            return apology("not enough shares to sell", 400)

        else:

            sell_symbol = request.form.get("symbol")
            sell_shares = int(request.form.get("shares"))

            user_info = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
            sell_info = lookup(sell_symbol)
            new_cash = user_info[0]["cash"] + (sell_info["price"] * int(sell_shares))

            if sell_portfolio[0]["shares"] - int(sell_shares) == 0:
                update_portfolio = db.execute("DELETE FROM portfolio WHERE user_id = ? AND symbol = ?",
                                              session["user_id"], sell_symbol)

            else:
                update_portfolio = db.execute("UPDATE portfolio SET shares = ? WHERE user_id = ? AND symbol = ?",
                                              (sell_portfolio[0]["shares"] - int(sell_shares)), session["user_id"], sell_symbol)

            # Get the date info
            today = date.today()

            # Store it as mm/dd/yy
            action_date = today.strftime("%m/%d/%Y")

            # Get the time info
            time = datetime.now()

            # Store it as hour:minute:second
            action_time = time.strftime("%H:%M:%S")

            # Calculate the amount spent
            amount = sell_info["price"] * int(sell_shares)

            # Record the whole action into the transactions table
            record_action = db.execute("INSERT INTO transactions (user_id, action_type, money, shares_amount, symbol, date, time) VALUES (?, 'sell', ?, ?, ?, ?, ?)",
                                       session["user_id"], amount, sell_shares, sell_info["symbol"], action_date, action_time)

            update_user = db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, session["user_id"])

            flash('Shares Sold!')
            return redirect("/")


@app.route("/addcash", methods=["GET", "POST"])
def addcash():

    # If the request is GET...
    if request.method == "GET":
        return render_template("addcash.html")

    # Else if the request is POST
    else:
        amount = int(request.form.get("cash"))

        # Get user money
        user_info = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        user_money = user_info[0]["cash"]

        # Update user money
        update = db.execute("UPDATE users SET cash = ? WHERE id = ?", user_money+amount, session["user_id"])

        flash("Money added!")

        return redirect("/")


@app.route("/changepass", methods=["GET", "POST"])
def changepass():

    # If the request is GET...
    if request.method == "GET":
        return render_template("changepass.html")

    # Else if the request is POST
    else:
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")

        user_info = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        user_password = user_info[0]["hash"]

        if not old_password or not new_password or not confirm_password:
            return apology("Please provide the password(s)", 403)

        # Compare passwords
        elif new_password != confirm_password:
            return apology("Can't confirm new password", 403)

        elif not check_password_hash(user_password, old_password):
            return apology("Can't confirm old password", 403)

        else:
            db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(new_password), session["user_id"])
            flash("Password changed successfully!")
            return redirect("/")