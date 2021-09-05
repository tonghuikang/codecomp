import argparse, requests, time
from bs4 import BeautifulSoup


DIRECTORY = "./"  # directory to save your samples
RETRY_INTERVAL = 10  # time interval in seconds to retrun
RETRY_COUNT = 10  # how many times to retry


def remove_until_first_line_break(s):
    return s[s.index('\n')+1:]


def parse_url(url, retries=RETRY_COUNT):
    try:
        html = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Connection error while getting url")
        time.sleep(RETRY_INTERVAL)
        print("Retrying")
        parse_url(url, retries=retries-1)
        return

    soup = BeautifulSoup(html.text, "html.parser")

    for problem in soup.find_all(class_="problem-statement"):
        title = problem.find(class_="header").find(class_="title").text
        question_number = title.split(".")[0].strip().lower()
        inputs = problem.find_all(class_="input")
        outputs = problem.find_all(class_="output")

        print("Found problem {} with {} sample cases".format(
            question_number, min(len(inputs),len(outputs))))

        if len(inputs) != len(outputs):
            print("Problem {} has different number of inputs and outputs".format(title))

        sep = ""  # for subproblems
        if question_number[-1] in "0123456789":
            sep += "_"

        for case_num, (input_,output_) in enumerate(zip(inputs, outputs), start=1):
            with open("{}/{}{}{}".format(DIRECTORY, question_number, sep, case_num), "w") as f:
                f.write(remove_until_first_line_break(input_.text))
            with open("{}/{}{}{}.out".format(DIRECTORY, question_number, sep, case_num), "w") as f:
                f.write(remove_until_first_line_break(output_.text))

    print("Done")


if __name__ == "__main__":
    '''
    Usage "python3 sample_crawl_cf.py 1480"

    You can test with contest ID 1480, which is Codeforces Round #700 Div. 2.
    The contest has both subproblems and multiple test cases
    '''
    parser = argparse.ArgumentParser(description='Parse the sample cases from a Codeforces contest')
    parser.add_argument('contest_id', type=int,
                        help="The Codeforces contest ID is found in the url")
    parser.add_argument('retry', default=False, action="store_true",
                        help="Whether to retry upon failure to connect")
    args = vars(parser.parse_args())
    url = 'https://codeforces.com/contest/{}/problems'.format(args['contest_id'])

    parse_url(url)