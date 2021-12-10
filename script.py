import urllib.request
import csv
import matplotlib.pyplot as plt

BASE_URL = "https://data.incovid19.org/"
CASE_TIME_SERIES = BASE_URL+"csv/latest/case_time_series.csv"
STATES = BASE_URL+"csv/latest/states.csv"
DISTRICTS	= BASE_URL+"csv/latest/districts.csv"
SOURCES_LIST	= BASE_URL+"csv/latest/sources_list.csv"
COWIN_VACCINE_DATA_STATEWISE	= BASE_URL+"csv/latest/cowin_vaccine_data_statewise.csv"
COWIN_VACCINE_DATA_DISTRICTWISE	= BASE_URL+"csv/latest/cowin_vaccine_data_districtwise.csv"
STATE_WISE_DAILY	= BASE_URL+"csv/latest/state_wise_daily.csv"
STATE_WISE	= BASE_URL+"csv/latest/state_wise.csv"
DISTRICT_WISE	= BASE_URL+"csv/latest/district_wise.csv"

#f = urllib2.urlopen(STATE_WISE_DAILY)
#cr = csv.reader(f)
r = urllib.request.urlretrieve(STATE_WISE_DAILY,'temp.csv')

def getCases(state_code):
    with open('temp.csv','r') as csvfile:
        date = []
        cases = []
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        state = -1
        state = fields.index(state_code)
        
        for row in csvreader:
            if('Confirmed' in row):
                date.append(str(row[0]))
                cases.append(int(row[state]))
        
        return cases

#print(date)
#print(cases)

#we truncate at the very end so as to maintain the originality of data
#plot y for last n days
def plot(y,n,ax):
    x = list(range(len(y[-n:])))
    x.reverse()
    x = [i*-1 for i in x]
    ax.plot(x,y[-n:])
#plot()

def nday_moving_avg(n,mylist):
    ret = []
    count = 0
    first_avg = 0
    list_len = len(mylist)
    for i in range(n):
        first_avg = first_avg + mylist[i]
    first_avg = first_avg/n
    for i in range(len(mylist)):
        if(count < n):
            count = count + 1
        else:
            #print(first_avg)
            ret.append(first_avg)
            first_avg = (first_avg*n - mylist[i-n]+mylist[i])/n
    ret.append(first_avg)
    return ret

LAST_N_DAYS = int(input("Last N days of data, N is: "))
N_DAY_AVG = int(input("N - Day moving average N is: "))

def plotState(state,ax):
    cases = getCases(state)
    n_day = nday_moving_avg(N_DAY_AVG,cases)
    plot(n_day,LAST_N_DAYS,ax)
    ax.set_title(state)
    

while True:
    fig, ax = plt.subplots(1,2)
    plotState("KA",ax[0])
    plotState("BR",ax[1])
    plt.show()
    LAST_N_DAYS = int(input("Last N days of data, N is: "))
    N_DAY_AVG = int(input("N - Day moving average N is: "))
    

# custom_xlim = (-LAST_N_DAYS,0)
# custom_ylim = (0,1400)
# plt.setp(ax,ylim=custom_ylim)
