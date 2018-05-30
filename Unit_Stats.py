#Internal Functions - see Kiting-RTS-Influence-Maps.pdf for definitions of these Functions
#dMax
#canKite
#order of stats: speed, acceleration, deceleration, turn, windUp, windDown, attackRange, HP, DPS,
import math

class UnitStats:
    Reaper = {'speed' : 3.75, 'acceleration' : 1000, 'deceleration' : 0, 'turnRate' : 999.8437, 'windUp' : 1.1, 'windDown' : .75, 'attackRange' : 5, 'HP' : 60, 'DPS' : 7.27}
    enemyStats = {'Zergling' : Zergling}
    Zergling = {'speed' : 2.95, 'creepSpeed' : 3.84, 'acceleration' : 1000, 'deceleration' : 0, 'turnRate' : 999.8437, 'windUp' : 0.696, 'windDown' : .5, 'attackRange' : 0.1, 'HP' : 35, 'DPS' : 7.14, 'tactical_threat' : 1,}

    def kiting_time():

        return Reaper['windUp'] + (1/Reaper['acceleration']) + (2 * math.pi  * (1/Reaper['turnRate']))


    def can_kite(target): # target is a string; eg. 'Zergling'

        reaperFaster = Reaper['speed'] > enemyStats[target]['speed']
        reaperOutrange = Reaper['attackRange'] > enemyStats[target]['attackRange'] + (enemyStats[target][speed] * kitingTime())

    def d_max(target): # target is a string; eg. 'Zergling'

      k = 1; #confidence constant value, can be adjusted
      return enemyStats[target.name]['attackRange'] + k + (enemyStats[target.name][speed] * kitingTime())
