import csv
import datetime
from os import listdir, makedirs
from os.path import isfile, join, exists

# Configuration
DATA_DIR = '/Users/greg/workspace/stargazers-utils/tests/data'
OUTPUT_DIR = '/Users/greg/workspace/stargazers-utils/tests'


class ContactInfo:
    """
    Creates a CSV containing the contact information of all users who starred the repository.
    """

    def __init__(self):
        """

        """

    def run(self):
        """

        :return:
        """
        data_files = self.__find_files()

        print 'test'

    def __find_files(self):
        """

        :return:
        """
        data_files = []
        for f in listdir(DATA_DIR):
            if f.startswith('https-api-github-com-users-') and not f.endswith(('-followers', '-starred', '-subscriptions')):
                data_files.append(join(DATA_DIR, f))

        return data_files


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    contact_info = ContactInfo()
    contact_info.run()
