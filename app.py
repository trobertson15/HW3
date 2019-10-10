from flask import Flask
from flask import render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Loan Payment Calculator')

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        form = request.form
        NoOfYears = int(form['NoOfYears'])
        PaymentsPerYear = int(form['PaymentsPerYear'])
        calc = NoOfYears*PaymentsPerYear
        PeriodicPayments = ("Total Periodic Payments: " + str(calc))
        return render_template('index.html', display=PeriodicPayments, pageTitle='Loan Payment Calculator')

@app.route('/divide', methods=['GET', 'POST'])
def divide():
    if request.method == 'POST':
        form = request.form
        PaymentsPerYear = int(form['PaymentsPerYear'])
        AnnualRate = float(form['AnnualRate'])
        calc = AnnualRate / PaymentsPerYear
        PeriodicRate = ("Periodic Interest Rate: " + str(calc))
        return render_template('index.html', display=PeriodicRate, pageTitle='Loan Payment Calculator')

@app.route('/discountfactor', methods=['GET', 'POST'])
def discountfactor():
    if request.method == 'POST':
        form = request.form
        NoOfPayments = float(form['NoOfPayments'])
        InterestRate = float(form['InterestRate'])
        calc = ((( 1 + InterestRate ) **NoOfPayments ) - 1 ) / ( InterestRate*( 1+ InterestRate) **NoOfPayments)
        DiscountFactor = ("Discount Factor: " + str(round(calc, 4)))
        return render_template('index.html', display=DiscountFactor, pageTitle='Loan Payment Calculator')


@app.route('/calculation', methods=['GET', 'POST'])
def calculation():
    if request.method == 'POST':
        form = request.form
        A = float(form['LoanAmount'])
        D = float(form['DiscountFactor'])
        calc = A / D
        LoanPayment = ("Loan Payment: $" + str(round(calc, 2)))
        return render_template('index.html', display=LoanPayment, pageTitle='Loan Payment Calculator')

if __name__ == '__main__':
    app.run(debug=True)
