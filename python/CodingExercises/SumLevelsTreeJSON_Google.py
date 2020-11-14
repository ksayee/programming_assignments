'''
Given:
          3
        / | \
       1  5  9
      /  / \  \
     6  1   4  5
Assume that this tree is contained in an input file data.json with the following format:
[
  {
    'value': 3,
    'children': [
      {
        'value': 1,
        'children': [
          {
            'value': 6,
            'children': []
          }
        ]
      },
      {
        'value': 5,
        'children': [
          {
            'value': 1,
            'children': []
          },
          {
            'value': 4,
            'children': []
          }
        ]
      },
      {
        'value': 9,
        'children': [
          {
            'value': 5,
            'children': []
          }
        ]
      }
    ]
  }
]
'''

def GetData_recur(output_lst,val):
    output_lst=[]
    for element in val:
        if len(element['children'])>0:
            output_lst.append(element['value'])
            output_lst.append(GetData_recur(output_lst,element['children']))
        else:
            output_lst.append(element['value'])
    return output_lst

def SumLevelsTreeJSON_Google(json_data):
    output_lst=[]
    for element in json_data:
        if len(element['children'])>0:
            output_lst.append(element['value'])
            output_lst.append(GetData_recur(output_lst,element['children']))
        else:
            output_lst.append(element['value'])
    sum_lst=[]
    print(output_lst)
    while len(output_lst)!=0:
        tmp=[]
        sum=0
        for val in output_lst:
            if isinstance(val,list):
                tmp.extend(val)
            else:
                sum=sum+val
        sum_lst.append(sum)
        output_lst=tmp.copy()
    return sum_lst

def main():

    json_data=[
  {
    'value': 3,
    'children': [
      {
        'value': 1,
        'children': [
          {
            'value': 6,
            'children': []
          }
        ]
      },
      {
        'value': 5,
        'children': [
          {
            'value': 1,
            'children': []
          },
          {
            'value': 4,
            'children': []
          }
        ]
      },
      {
        'value': 9,
        'children': [
          {
            'value': 5,
            'children': []
          }
        ]
      }
    ]
  }
]
    print(SumLevelsTreeJSON_Google(json_data))

if __name__=='__main__':
    main()