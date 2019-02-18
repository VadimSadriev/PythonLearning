from flask import Flask, render_template,request, redirect, escape, copy_current_request_context
import defModule
import mysql.connector
from Dbcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from threading import Thread
from time import sleep

app = Flask(__name__)
# session allows to store state for example - user logged in site or not

# dbConfig = {'host': '127.0.0.1',
#             'user': 'Anotsu',
#             'password': 'Zver514779000',
#             'database': 'mainLogDb'}

app.config['dbconfig'] = {'host': '127.0.0.1',
            'user': 'Anotsu',
            'password': 'Zver514779000',
            'database': 'mainLogDb'}


# @app.route('/')
# def hello() -> str:
#     return redirect('/entry')


@app.route('/search4', methods=['POST'])
def do_search():
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        sleep(15)
        with open('mainLog.log', 'a') as log:
            # print(str(dir(req)), res, file=log)
            # print(req.form, file=log, end='|')
            # print(req.remote_addr, file=log, end='|')
            # print(req.user_agent, file=log, end='|')
            # print(res, file=log)
            print(req.form, req.remote_addr, req.user_agent, req, file=log, sep='|')
        # conn = mysql.connector.connect(**dbConfig)
        # cursor = conn.cursor()
        # _SQL = """insert into log
        #         (phrase, letters, ip, browser_string, results)
        #         values
        #         (%s, %s, %s, %s, %s)"""
        # cursor.execute(_SQL, (req.form['phrase'],
        #                       req.form['letters'],
        #                       req.remote_addr,
        #                       req.user_agent.browser,
        #                       res,))
        # conn.commit()
        # cursor.close()
        # conn.close()
        try:
            with UseDatabase(app.config['dbconfig']) as cursor:
                _SQL = """insert into log
                        (phrase, letters, ip, browser_string, results)
                        values
                        (%s, %s, %s, %s, %s)"""
                cursor.execute(_SQL, (req.form['phrase'],
                                      req.form['letters'],
                                      req.remote_addr,
                                      req.user_agent.browser,
                                      res,))
        except ConnectionError as err:
            print(str(err))
        except CredentialsError as err:
            print(str(err))
        except Exception as err:
            print(str(err))

    title = 'Here are ur results'
    phrase= request.form['phrase']
    letters= request.form['letters']
    results = defModule.search4letter(phrase, letters).__str__()
    try:
       # log_request(request, results)
       t = Thread(target=log_request, args=(request, results))
       t.start()
    except ConnectionError as err:
        print(str(err))
    except Exception as err:
        print(str(err))
    return render_template('results.html', the_results=results,
                           the_phrase=phrase,
                           the_letters= letters,
                           the_title=title)

@app.route('/')
@app.route('/entry')
def index() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> 'html':
    # with open('mainLog.log') as log:
    #     contents = escape(log.read())
    # return contents
    # contents = []
    # with open('mainLog.log') as log:
    #     for line in log:
    #         contents.append([])
    #         for item in line.split('|'):
    #             contents[-1].append(escape(item))
    # titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    # #return str(contents)
    # return render_template('viewlog.html',
    #                        the_title='View log',
    #                        the_row_titles=titles,
    #                        the_data=contents)
   try:
       with UseDatabase(app.config['dbconfig']) as cursor:
           _SQL = """select phrase, letters, ip, browser_string, results
               from log"""
           cursor.execute(_SQL)
           contents = cursor.fetchall()
           titles = ('Phrase', 'Letters', 'remote_addr', 'user_agent', 'results')
           return render_template('viewlog.html',
                                  the_title='View log',
                                  the_row_titles=titles,
                                  the_data=contents)
   except ConnectionError as err:
       print(str(err))
   except CredentialsError as err:
       print(str(err))
   except SQLError as err:
       print(str(err))
   except Exception as err:
       print(str(err))




if __name__ == '__main__':
    app.run(debug=True)