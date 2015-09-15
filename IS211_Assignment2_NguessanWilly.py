
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment2. Working with different modules."""

import urllib2
import csv
import datetime
import logging
import argparse
import sys


def main():
    """get the CSV file and stores in a dictionary."""

    def downloadData(url):
        """import file."""
        get_url = urllib2.urlopen(url)
        return get_url

    def processData(data):
        """Process the data and store in a dictionary."""
        csvFichier = csv.reader(data)
        persondict = {}
        csvFichier.next()

        for ligne in csvFichier:
            try:
                ligne[2] = datetime.datetime.strptime(ligne[2], "%d/%m/%Y")
            except ValueError:
                numero = int(ligne[0])
                line = int(ligne[0])+1
                logger = logging.getLogger(" assignment2")
                logger.error(" Error processing line #{} for ID #{}.".format(line, numero))

            persondict[int(ligne[0])] = (ligne[1], ligne[2])
        return persondict

    def displayPerson(id, personData):
        """Display a person's info."""
        try:
            response = "Person #{idnum} is {name} with a birthday of {date}"
            print response.format(idnum=id, name=personData[id][0], date=personData[id][1])
        except KeyError:
            print "No person found with that ID #."

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="The URL that will look for the file.")
    args = parser.parse_args()
    logging.basicConfig(filename="errors.log", level=logging.ERROR)

    if args.url:
        csvData = downloadData(args.url)
        personData = processData(csvData)
        msg = "Please enter an ID #. Enter 0 or a negative # to exit. "

        while True:
            try:
                user = int(raw_input(msg))
            except ValueError:
                print "Invalid input. Please try again."
                continue
            if user > 0:
                displayPerson(user, personData)
            else:
                print "Hope you enjoyed,Thank You ."
                sys.exit()
    else:
        print "Please use the --url parameter."

if __name__ == "__main__":
    main()
