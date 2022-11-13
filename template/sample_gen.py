import json, cgi
from sys import argv
from http.server import BaseHTTPRequestHandler, HTTPServer


DIRECTORY = "./"    # directory to save your samples
question_count = 0  # I could not make it an instance variable
                    # https://stackoverflow.com/questions/18444395/


sites_with_unnumbered_questions = set([
    "codechef.com", "facebook.com", "google.com",
])
    

def save_test_case(question, question_count=0):
    
    for substring in sites_with_unnumbered_questions:
        if substring in question["url"]:
            question_number = "abcdefghi"[question_count%9]
            break
    else:
        question_number = question["name"].replace('-', '.').split(".")[0].strip().lower()
    
    print("Found problem {} with {} sample cases".format(
        question_number, len(question["tests"])))

    sep = ""  # for subproblems
    if question_number[-1] in "0123456789":
        sep += "_"
    
    for case_num, test_case in enumerate(question["tests"], start=1):
        with open("{}/{}{}{}".format(DIRECTORY, question_number, sep, case_num), "w") as f:
            f.write(test_case['input'])
        with open("{}/{}{}{}.out".format(DIRECTORY, question_number, sep, case_num), "w") as f:
            f.write(test_case['output'])


class Server(BaseHTTPRequestHandler):
    
    def __init__(self, *args):
        super().__init__(*args)

    def do_POST(self):
        # define action on receiving POST request
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

        # refuse to receive non-json content
        if ctype != 'application/json':
            print("Non JSON content received")
            self.send_response(400)
            self.end_headers()
            return

        # read the message and convert it into a python dictionary
        length = int(self.headers.get('content-length'))
        question = json.loads(self.rfile.read(length))
        global question_count
        save_test_case(question, question_count=question_count)
        question_count += 1


def run(server_class=HTTPServer, handler_class=Server, port=10007):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.allow_reuse_address = True

    try:
        print('Starting httpd on port {}...'.format(port))
        httpd.serve_forever()
    except:
        # shutdown to free used port
        print('Shutting down.')
        httpd.shutdown()


if __name__ == "__main__":
    '''
    Usage
    
    Install Chrome extension
    https://chrome.google.com/webstore/detail/competitive-companion/cjnmckjndlpiamhfimnnjmnckgghkjbl
    
    Change port address to 10007 or otherwise
    chrome://extensions/?options=cjnmckjndlpiamhfimnnjmnckgghkjbl
    
    Run this script
    python3 sample_gen.py
    
    Download tasks from contest website
    https://codeforces.com/contest/1480/
    https://codeforces.com/contest/1480/problem/D1
    https://atcoder.jp/contests/arc118/tasks
    https://atcoder.jp/contests/arc118/tasks/arc118_a
    https://www.codechef.com/LTIME95B/problems/CCHEAVEN
    https://www.facebook.com/codingcompetitions/hacker-cup/2020/round-2/problems/A
    https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae4aa
    https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882
    '''
    
    if len(argv) == 2:  # if the port is specified
        run(port=int(argv[1]))
    else:
        run()
