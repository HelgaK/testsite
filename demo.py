# -*- coding: utf-8 -*-
import flask, flask.views
import calc_staj

app = flask.Flask(__name__)
# Don't do this!
app.secret_key = "bacon"

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
        
    def post(self):
        input_str = str(flask.request.form['expression1'])
        parts_of_input = input_str.split(',')
        start_data_str = parts_of_input[0].strip()
        finish_data_str = parts_of_input[1].strip()
        out_str = "\nstart\n"
        out_str += start_data_str
        out_str += "\nstop\n"
        out_str += finish_data_str
        res_of_calc = calc_staj.calc_staj_in_days(start_data_str,finish_data_str)

        flask.flash(out_str + "\nstaj:\n" + str(res_of_calc) + " dney.")
        return self.get()
    
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.debug = True
app.run()