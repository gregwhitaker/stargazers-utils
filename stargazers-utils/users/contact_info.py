import csv
import json
from os import listdir, makedirs
from os.path import isfile, join, exists

# Configuration
DATA_DIR = '/Users/greg/workspace/stargazers-utils/tests/data'
OUTPUT_DIR = '/Users/greg/workspace/stargazers-utils/tests'
OUTPUT_FILENAME = 'contact_info.csv'


class ContactInfo:
    """
    Creates a CSV containing the contact information of all users who starred the repository.
    """

    def __init__(self):
        with open(join(OUTPUT_DIR, OUTPUT_FILENAME), 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['login', 'name', 'email', 'company', 'bio', 'location'])

    def run(self):
        """

        :return:
        """
        data_files = self.__find_files()

        if not data_files:
            print "No user data files found to process in: {0}".format(DATA_DIR)
            exit(1)

        processed_cnt = 0
        for f in data_files:
            print "Processing: {0}".format(f)
            json = self.__get_file_json(f)
            contact_data = self.__get_contact_data(json)
            self.__append_to_output_file(contact_data)

            processed_cnt += 1

        print "Processed {0} files".format(processed_cnt)

    def __find_files(self):
        """
        Finds user data files in the data directory of stargazers.
        :return: list of user data files to process
        """
        data_files = []
        for f in listdir(DATA_DIR):
            if f.startswith('https-api-github-com-users-') and not f.endswith(('-followers', '-starred', '-subscriptions')):
                data_files.append(join(DATA_DIR, f))

        return data_files

    def __get_file_json(self, f):
        """
        Strips the HTTP header off of the data file and returns a json string
        :param f: data file to process
        :return: json
        """
        with open(f, 'r') as data_file:
            found = False
            for line in data_file:
                if found:
                    return json.loads(line)
                else:
                    if len(line.strip()) == 0:
                        found = True

    def __get_contact_data(self, json):
        """

        :param data_str:
        :return:
        """
        contact_data = dict()
        contact_data['login'] = json['login']
        contact_data['name'] = json['name']
        contact_data['email'] = json['email']
        contact_data['company'] = json['company']
        contact_data['bio'] = json['bio']
        contact_data['location'] = json['location']

        return contact_data

    def __append_to_output_file(self, contact_data):
        """

        :param contact_data:
        :return:
        """
        with open(join(OUTPUT_DIR, OUTPUT_FILENAME), 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

            row = [contact_data['login'],
                   contact_data['name'],
                   contact_data['email'],
                   contact_data['company'],
                   contact_data['bio'],
                   contact_data['location']]

            writer.writerow(row)


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    contact_info = ContactInfo()
    contact_info.run()
