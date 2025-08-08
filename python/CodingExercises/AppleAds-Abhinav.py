from typing import List
import pprint
"""
PROMPT:
A city is planning to safely demolish an old skyscraper.
The building is structured in a way where each floor
may directly support zero or more other floors above it.

You must compute the demolition plan as a list of demolition rounds.
In each round, you should specify the floors that can be safely
demolished at that time. Continue until all floors are removed,
and the building is entirely demolished.

To ensure safety, a floor can only be demolished if it has
no floors above it.

You will be given the ground-level Floor as an input. This Floor
is guaranteed to be non-null.

EXAMPLES:

Example 1

   ________
  [  Fl E  ]
  [  Fl D  ]
  [  Fl C  ]
  [  Fl B  ]
  [  Fl A  ]
  ----------

Expected Result:
[
   [ E ],
   [ D ],
   [ C ],
   [ B ],
   [ A ],
]

Example 2
           ___________
          [    Fl L   ]
   _______[    Fl K   ]_______
  [            Fl J           ]
  [   Fl H   ]     [   Fl I   ]
  [   Fl F   ]     [   Fl G   ]
  [   Fl D   ]     [   Fl E   ]
  [   Fl B   ]_____[   Fl C   ]
  [          Floor A          ]
  -----------------------------

Expected Result:
[
   [ L ],
   [ K ],
   [ J ],
   [ H, I ],
   [ F, G ],
   [ D, E ],
   [ B, C ],
   [ A ]
]


Example 3
   ________
  [  Fl J  ] ________
  [  Fl H  ][  Fl I  ] ________
  [  Fl E  ][  Fl F  ][  Fl G  ]
  [  Fl B  ][  Fl C  ][  Fl D  ]
  [          Floor A           ]
  ------------------------------

Expected Result:
[
   [ J, I, G ],
   [ H, F, D ],
   [ E, C ]
   [ B ],
   [ A ]
]

"""
class Floor:
    def __init__(self, id: str):
        self.id = id
        self.supported_floors: List['Floor'] = []

    def DemolishBuilding(self,obj):
        output_lst=[]
        output_lst.append(obj.id)

        for upper_floor in obj.supported_floors:
            tmp_lst=[]
            self.GetFloors_recur(upper_floor,tmp_lst)
            output_lst.append(tmp_lst.copy())

        return self.GetSequenceDemolision(output_lst)

    def GetFloors_recur(self,floor,tmp_lst):
        tmp_lst.append(floor.id)
        for upper_floor in floor.supported_floors:
            self.GetFloors_recur(upper_floor,tmp_lst)

    def GetSequenceDemolision(self,output_lst):
        demolish_seq_lst=[]
        start = 1
        end = len(output_lst)-1
        while True:
            tmp_lst=[]
            while start <=end:
                if len(output_lst[start])>0:
                    if output_lst[start][-1] not in tmp_lst:
                        tmp_lst.append(output_lst[start][-1])
                    output_lst[start].pop()
                start = start + 1

            if len(tmp_lst)>0:
                demolish_seq_lst.append(tmp_lst.copy())
                start = 1
            else:
                break

        tmp_lst=[]
        tmp_lst.append(output_lst[0])
        demolish_seq_lst.append(tmp_lst.copy())

        return demolish_seq_lst

def main():

  """
  Example 1
     ________
    [  Fl E  ]
    [  Fl D  ]
    [  Fl C  ]
    [  Fl B  ]
    [  Fl A  ]
    ----------
  """
  fA = Floor("A")
  fB = Floor("B")
  fC = Floor("C")
  fD = Floor("D")
  fE = Floor("E")

  fA.supported_floors.append(fB)
  fB.supported_floors.append(fC)
  fC.supported_floors.append(fD)
  fD.supported_floors.append(fE)
  pprint.pprint(fA.DemolishBuilding(fA))

  """
  Example 3
     ________
    [  Fl J  ] ________
    [  Fl H  ][  Fl I  ] ________
    [  Fl E  ][  Fl F  ][  Fl G  ]
    [  Fl B  ][  Fl C  ][  Fl D  ]
    [          Floor A           ]
    ------------------------------
  """

  fA = Floor("A")
  fB = Floor("B")
  fC = Floor("C")
  fD = Floor("D")
  fE = Floor("E")
  fF = Floor("F")
  fG = Floor("G")
  fH = Floor("H")
  fI = Floor("I")
  fJ = Floor("J")

  fA.supported_floors.extend([fB, fC, fD])
  fB.supported_floors.append(fE)
  fC.supported_floors.append(fF)
  fD.supported_floors.append(fG)
  fF.supported_floors.append(fI)
  fE.supported_floors.append(fH)
  fH.supported_floors.append(fJ)
  pprint.pprint(fA.DemolishBuilding(fA))

  """
  Example 2
             ___________
            [    Fl L   ]
     _______[    Fl K   ]_______
    [            Fl J           ]
    [   Fl H   ]     [   Fl I   ]
    [   Fl F   ]     [   Fl G   ]
    [   Fl D   ]     [   Fl E   ]
    [   Fl B   ]_____[   Fl C   ]
    [          Floor A          ]
    -----------------------------
  """

  fA = Floor("A")
  fB = Floor("B")
  fC = Floor("C")
  fD = Floor("D")
  fE = Floor("E")
  fF = Floor("F")
  fG = Floor("G")
  fH = Floor("H")
  fI = Floor("I")
  fJ = Floor("J")
  fK = Floor("K")
  fL = Floor("L")

  fA.supported_floors.extend([fB, fC])
  fB.supported_floors.append(fD)
  fC.supported_floors.append(fE)
  fD.supported_floors.append(fF)
  fE.supported_floors.append(fG)
  fG.supported_floors.append(fI)
  fI.supported_floors.append(fJ)
  fF.supported_floors.append(fH)
  fH.supported_floors.append(fJ)
  fJ.supported_floors.append(fK)
  fK.supported_floors.append(fL)
  pprint.pprint(fA.DemolishBuilding(fA))

if __name__ == "__main__":
  main()