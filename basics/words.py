#! /usr/local/bin/python
import sys
import urllib


def fetch_words(url):
    """Function to fetch data from url

    Args:
        url (str): url from which to fetch data

    Returns:
        [type]: [description]
    """
    story = urllib.urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_words(story_words):
    """Print items function

    Args:
        story_words ([str]): An array of story words
    """
    for word in story_words:
        print(word)


def main(url):
    """main function

    Args:
        url (str): url to fetch words from
    """
    words = fetch_words(url)
    print_words(words)


if __name__ == '__main__':
    main(sys.argv[1])
