-- Keep a log of any SQL queries you execute as you solve the mystery.

-- This command will lead me to the crimes happened on the same day.
SELECT * FROM crime_scene_reports WHERE year = 2021 AND  month = 7 AND day = 28;

-- CLUE: Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted
-- today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.

-- Our case's id is 295.
-- Three witnesses that have interviews
-- I should get the interviews, but how?

-- I will check the interviews happened on the same day.
SELECT id, transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;
-- I found 7 interviews, three of them seems like quotes from the book, Sherlock Holmes...
-- The last one also seems irrelevant.
-- So, #161, 162, and 163 can lead me somewhere...

-- 161: Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

-- I do have security footage, this can lead me to another clue.
-- But let me read the other interviews.
-- Also, I realized that I can see the names of the each interview, so let's find the names from the relevant ones.

SELECT name, transcript FROM interviews WHERE id = 161;
-- I get the name Ruth from the interview #161.

-- 161 | Ruth | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame. |

-- CLUE: Security footage from the bakery's parking lot might have caught the licence plate of the thief.

SELECT name, transcript FROM interviews WHERE id = 162;
-- 162 | Eugene | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
-- I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money. |

-- CLUE: Thief withdrew money from the ATM on Leggett Street this morning.

SELECT name, transcript FROM interviews WHERE id = 163;
-- 163 | Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
-- The thief then asked the person on the other end of the phone to purchase the flight ticket. |

-- CLUE: Thief was talking on the phone while leaving the bakery.
-- The call wasn't too long, less than a minute.
-- They were trying to leave Fiftyville ASAP, so they agreed to buy flight tickets.

-- I believe those clues can lead me.
-- First, let's start with security footage:

SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28;
-- Too many activities happened on that day.

-- But let me stop there for a moment, I realized something.
-- All the interviews about our case have the word "bakery" in transcript.
-- I should also check the transcripts that have the word "bakery".
SELECT id, name, transcript FROM interviews WHERE transcript LIKE '%bakery%';
-- I found another interview that includes the word "bakery", but it was irrelevant.
-- It was about a guy named Richard, whose pastry was stolen.

-- Let's go back the logs...
-- The theft happened at 10:15am. I should check who were in the bakery in that time.
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute < 26 AND activity = 'exit';
-- 8 cars were here, let's find the owners.
SELECT name FROM people WHERE license_plate IN (SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute < 26 AND activity = 'exit');
-- 'Vanessa', 'Barry', 'Iman', 'Sofia', 'Luca', 'Diana', 'Kelsey', 'Bruce'

-- Let's check second interview, the one that about the phone call.
SELECT * FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;
-- 9 results
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60) OR phone_number IN (SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60);
--'Sofia', 'Diana', 'Kelsey', 'Bruce'
-- 4 common names

--Let's check the ATM transactions.
SELECT account_number FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location LIKE '%Leggett%';
-- Let's find the owners
SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location LIKE '%Leggett%'));
-- 'Diana', 'Bruce'
-- 2 remaining suspects

-- Let's find the earliest flight of the next morning and who were in that flight.
-- But first, let's find Fiftyville's airport id.
SELECT id FROM airports WHERE city = 'Fiftyville';
-- airport_id = 8

SELECT * FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = 8;
-- Earliest flight was from Fiftville to airport_id = 4, flight_id = 36
SELECT city FROM airports WHERE id = 4;
-- The destination was New York City

SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);
-- Bruce is the thief
-- Who was Bruce was talking with on the phone?
-- Let's find Bruce's phone number.

SELECT phone_number FROM people WHERE name = 'Bruce';
-- (367) 555-5533

SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE receiver = '(367) 555-5533' AND year = 2021 AND month = 7 AND day = 28 AND duration < 60) OR phone_number IN (SELECT receiver FROM phone_calls WHERE caller = '(367) 555-5533' AND year = 2021 AND month = 7 AND day = 28 AND duration < 60);
-- Robin