from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.
URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/
	
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/PlayersIndex')
def PlayersIndex():
	return render_template('Tables/PlayersIndex.html')

@app.route('/CoachesIndex')
def CoachesIndex():
	return render_template('Tables/CoachesIndex.html')

@app.route('/TeamsIndex')
def TeamsIndex():
	return render_template('Tables/TeamsIndex.html')

@app.route('/DAngelo_Russell')
def DAngelo_Russell():
	return render_template('Players/DAngelo_Russell.html')

@app.route('/Dwyane_Wade')
def Dwyane_Wade():
	return render_template('Players/Dwyane_Wade.html')

@app.route('/Isaiah_Thomas')
def Isaiah_Thomas():
	return render_template('Players/Isaiah_Thomas.html')

@app.route('/Jimmy_Butler')
def Jimmy_Butler():
	return render_template('Players/Jimmy_Butler.html')

@app.route('/Jordan_Clarkson')
def Jordan_Clarkson():
	return render_template('Players/Jordan_Clarkson.html')

@app.route('/Kawhi_Leonard')
def Kawhi_Leonard():
	return render_template('Players/Kawhi_Leonard.html')

@app.route('/Kevin_Durant')
def Kevin_Durant():
	return render_template('Players/Kevin_Durant.html')

@app.route('/Kevin_Garnett')
def Kevin_Garnett():
	return render_template('Players/Kevin_Garnett.html')

@app.route('/Kevin_Love')
def Kevin_Love():
	return render_template('Players/Kevin_Love.html')

@app.route('/Klay_Thompson')
def Klay_Thompson():
	return render_template('Players/Klay_Thompson.html')

@app.route('/Kobe_Bryant')
def Kobe_Bryant():
	return render_template('Players/Kobe_Bryant.html')

@app.route('/Kyrie_Irving')
def Kyrie_Irving():
	return render_template('Players/Kyrie_Irving.html')

@app.route('/LaMarcus_Aldridge')
def LaMarcus_Aldridge():
	return render_template('Players/LaMarcus_Aldridge.html')

@app.route('/Lebron_James')
def Lebron_James():
	return render_template('Players/Lebron_James.html')

@app.route('/Michael_Jordan')
def Michael_Jordan():
	return render_template('Players/Michael_Jordan.html')

@app.route('/Pau_Gasol')
def Pau_Gasol():
	return render_template('Players/Pau_Gasol.html')

@app.route('/Paul_Pierce')
def Paul_Pierce():
	return render_template('Players/Paul_Pierce.html')

@app.route('/Rajon_Rondo')
def Rajon_Rondo():
	return render_template('Players/Rajon_Rondo.html')

@app.route('/Stephen_Curry')
def Stephen_Curry():
	return render_template('Players/Stephen_Curry.html')

@app.route('/Boston_Celtics')
def Boston_Celtics():
	return render_template('Teams/Boston_Celtics.html')

@app.route('/Chicago_Bulls')
def Chicago_Bulls():
	return render_template('Teams/Chicago_Bulls.html')

@app.route('/Cleveland_Cavaliers')
def Cleveland_Cavaliers():
	return render_template('Teams/Cleveland_Cavaliers.html')

@app.route('/Golden_State_Warriors')
def Golden_State_Warriors():
	return render_template('Teams/Golden_State_Warriors.html')

@app.route('/LA_Lakers')
def LA_Lakers():
	return render_template('Teams/LA_Lakers.html')

@app.route('/SA_Spurs')
def SA_Spurs():
	return render_template('Teams/SA_Spurs.html')

@app.route('/Brad_Stevens')
def Brad_Stevens():
	return render_template('Coaches/Brad_Stevens.html')

@app.route('/Fred_Hoiberg')
def Fred_Hoiberg():
	return render_template('Coaches/Fred_Hoiberg.html')

@app.route('/Gregg_Popovich')
def Gregg_Popovich():
	return render_template('Coaches/Gregg_Popovich.html')

@app.route('/Luke_Walton')
def Luke_Walton():
	return render_template('Coaches/Luke_Walton.html')

@app.route('/Steve_Kerr')
def Steve_Kerr():
	return render_template('Coaches/Steve_Kerr.html')

@app.route('/Tyronn_Lue')
def Tyronn_Lue():
	return render_template('Coaches/Tyronn_Lue.html')

# @app.route('/page3')
# def page3():
# 	dict = {'string1' : 'Testing.', 'string2' : 'Hello, World!'}
# 	return render_template('page3.html', strings = dict) # Example of argument passing to HTML template
	
if __name__ == '__main__':
	app.run(port=5000) # Run application