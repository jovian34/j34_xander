BONUS = 52.5
xander_current = input('How much does Xander have now? ')
xander_current = float(xander_current)
madison_current = input('How much does Madison have now? ')
madison_current = float(madison_current)
tristan_current = input('How much does Tristan have now? ')
tristan_current = float(tristan_current)
 
xander_add = BONUS + tristan_current + madison_current - 2 * xander_current
xander_add = xander_add / 3
 
new_total = xander_add + xander_current
tristan_add = new_total - tristan_current
madison_add = new_total - madison_current
 
print('Xander needs: $', xander_add)
print('Madison needs: $', madison_add)
print('Tristan needs: $',tristan_add)
