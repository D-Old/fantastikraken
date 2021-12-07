# -*- coding: utf-8 -*-
import datetime
from dateutil.relativedelta import relativedelta


dt = datetime.datetime(2021, 12, 7)
startdate = dt
dtList = [dt]
NoOfTrees = 12
NewTreesPerMonth = 1
MaxTrees = 2000
decarb = 0.0025 # t, monthly 
footpr = 5/12 # t, monthly 
lifeExpectancy = datetime.datetime(2070, 12, 31)
TotEmish = 394 #32y10m
TotEmishList = [TotEmish]
KumEmish = TotEmish
KumEmishList = [KumEmish]
netZeroReached = 0

while TotEmish >= 0:
    dt = dt + relativedelta(months=+1)
    dtList.append(dt)
    if dt > lifeExpectancy:
      footpr = 0
    monthlyFootpr = footpr - NoOfTrees*decarb
    if monthlyFootpr < 0 and netZeroReached == 0:
        netZeroDay = dt
        netZeroReached = 1
    KumEmish = KumEmish + max(0, monthlyFootpr)
    TotEmish = TotEmish + monthlyFootpr
    TotEmishList.append(TotEmish)
    if NoOfTrees < MaxTrees:
        NoOfTrees = NoOfTrees + NewTreesPerMonth
        enddate = dt

PlantingPhase = relativedelta(enddate, startdate)

print('With', NoOfTrees, 'trees (', NoOfTrees*30, '€), planted in', PlantingPhase.years, 'years and', PlantingPhase.months, 'months (at', "{:.2f}".format(NoOfTrees*30/PlantingPhase.years), '€/year) all carbon is reabsorbed until', dt.strftime("%m"), '/',  dt.strftime("%Y"), 'which means it took', dt.year-2020, 'years.',
'Until becoming decarbonising in', netZeroDay.strftime("%m"), '/',  netZeroDay.strftime("%Y"),'the amount of CO2 emitted is', "{:.2f}".format(KumEmish), 't')
#print('With', NoOfTrees, 'trees (', NoOfTrees*30, '€), planted in', "{:.2f}".format(PlantingPhase), 'years (at', NoOfTrees*30/PlantingPhase, '€/year) all carbon is reabsorbed until', dt.strftime("%m"), '/',  dt.strftime("%Y"), 'which means it took', dt.year-2020, 'years.',
#'Until becoming decarbonising in', netZeroDay.strftime("%m"), '/',  netZeroDay.strftime("%Y"),'the amount of CO2 emitted is', "{:.2f}".format(KumEmish), 't')

import matplotlib.pyplot as plt
plt.plot(dtList, TotEmishList)

#end of file