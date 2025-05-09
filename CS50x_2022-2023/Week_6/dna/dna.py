import csv
import sys


def main():
    # Check arguments usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)
    # Read the database in arguments as a dictionary
    with open(sys.argv[1], "r") as db:
        reader = csv.DictReader(db)
        database = list(reader)
    # Read the sequence in arguments
    with open(sys.argv[2], "r") as seq:
        sequence = seq.read()

    # Create a dictionary called matches
    matches = {}

    # Check the database and write the longest match to matches
    for i in database[0]:
        matches[i] = (longest_match(sequence, i))

    # Counter starts from 1, because 'name' isn't a match
    counter = 1
    suspect = "No match"

    for i in range(len(database)):
        for j in matches:
            # Convert matches to strings for comparison
            if str(matches[j]) == database[i][j]:
                counter += 1
        if counter == len(matches):
            # Break the loop if suspect is found
            suspect = database[i]['name']
            break
        else:
            # Else, set counter to 1 again and continue
            counter = 1

    print(suspect)

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
