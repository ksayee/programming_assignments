
def min_by_key(key, records):
    """
    Step 1
    key,direction, records
    'a',asc,records
    'a,'',records

    Throughout this interview, we'll pretend we're building a new analytical
    database. Don't worry about actually building a database though – these will
    all be toy problems.

    Here's how the database works: all records are represented as maps, with string
    keys and integer values. The records are contained in an array, in no
    particular order.

    To begin with, the database will support just one function: min_by_key. This
    function scans the array of records and returns the record that has the minimum
    value for a specified key. Records that do not contain the specified key are
    considered to have value 0 for the key. Note that keys may map to negative values!

    Here's an example use case: each of your records contains data about a school
    student. You can use min_by_key to answer questions such as 'who is the youngest
    student?' and 'who is the student with the lowest grade-point average?'

    Implementation Notes:
      - You should handle an empty array of records in an idiomatic way in
        your language of choice.
      - If several records share the same minimum value for the chosen key,
        you may return any of them.

    Examples:
      assert min_by_key('a', [{'a': 1, 'b': 2}, {'a': 2}]) == {'a': 1, 'b': 2}
      assert min_by_key('a', [{'a': 2}, {'a': 1, 'b': 2}]) == {'a': 1, 'b': 2}
      assert min_by_key('b', [{'a': 1, 'b': 2}, {'a': 2}]) == {'a': 2}
      assert min_by_key('a', [{}]) == {}
      assert min_by_key('a', []) == -1
      assert min_by_key('b', [{'a': -1}, {'b': -1}]) == {'b': -1}
    """
    return first_by_key(key, 'asc', records)

def first_by_key(key, direction, records):
    """
    Step 2
    Our next step in database development is to add a new function. We'll call this
    function first_by_key. It has much in common with min_by_key.  first_by_key
    takes three arguments:
    1. a string key
    2. a string sort direction (which must be either 'asc' or 'desc')
    3. an array of records, just as in min_by_key.
    If the sort direction is 'asc', then we should return the minimum record,
    otherwise we should return the maximum record. As before, records without a
    value for the key should be treated as having value 0.
    Once you have a working solution, you should re-implement min_by_key in terms
    of first_by_key .
    Examples:
      assert first_by_key('a', 'asc', [{'a': 1}]) == {'a': 1}
      assert first_by_key('a', 'asc', [{'b': 1}, {'b': -2}, {'a': 10}]) in [{'b': 1}, {'b': -2}]
      assert first_by_key('a', 'desc', [{'b': 1}, {'b': -2}, {'a': 10}]) == {'a': 10}
      assert first_by_key('b', 'asc', [{'b': 1}, {'b': -2}, {'a': 10}]) == {'b': -2}
      assert first_by_key('b', 'desc', [{'b': 1}, {'b': -2}, {'a': 10}]) == {'b': 1}
      assert first_by_key('a', 'desc', [{}, {'a': 10, 'b': -10}, {}, {'a': 3, 'c': 3}]) == {'a': 10, 'b': -10}
    """

    if len(records)==0:
        return -1

    if direction=='asc':
        flg=False
    elif direction=='desc':
        flg=True

    for dict in records:
        if key in dict.keys():
            continue
        else:
            dict[key]=0

    sort_list=sorted(records,key=lambda x:x[key],reverse=flg)
    for dict in sort_list:
        if dict[key]==0 and dict not in records:
            del dict[key]

    return sort_list[0]

class RecordComparator:
    """
    Step 3
    As we build increasingly rich orderings for our records, we'll find it useful
    to extract the comparison of records into a comparator. This is a function or
    object (depending on your language) which determines if a record is
    'less than', equal, or 'greater than' another.
    In object-oriented languages, you should write a class whose constructor
    accepts two parameters: a string key and a string direction. The class should
    implement a method compare that takes as its parameters two records. This
    method should return -1 if the first record comes before the second record
    (according to key and direction), zero if neither record comes before the
    other, or 1 if the first record comes after the second.
    In functional languages, you should write a function which accepts two
    parameters: a string key and a string direction. The function should return
    a function that takes as its parameters two records. This function should return
    -1 if the first record comes before the second record (according to key and
    direction), zero if neither record comes before the other, or 1 if the first
    record comes after the second.
    You should then use your comparator in your implementation of first_by_key.
    Examples:
      cmp = Comparator('a', 'asc')
      assert cmp.compare({'a': 1}, {'a': 2}) == -1
      assert cmp.compare({'a': 2}, {'a': 1}) == 1
      assert cmp.compare({'a': 1}, {'a': 1}) == 0
    """

    def __init__(self, key, direction):
        self.direction=direction
        self.key=key

    def compare(self, left, right):

        lst=[]
        lst.append(left)
        lst.append(right)

        if left[self.key]==right[self.key]:
            return 0

        if self.direction=='asc':
            flg=False
        else:
            flg=True

        sort_list=sorted(lst,key=lambda x:x[self.key],reverse=flg)

        if lst==sort_list:
            return -1
        else:
            return 1

def test_record_comparator():
    cmp = RecordComparator('a', 'asc')
    assert cmp.compare({'a': 1}, {'a': 2}) == -1
    assert cmp.compare({'a': 2}, {'a': 1}) == 1
    assert cmp.compare({'a': 1}, {'a': 1}) == 0

def assertIn(a, *b):
    assert a in b, "\nExpected:\n  %s\nIn:\n  %s\n" % (b, a)
    print('\033[92mPASSED\033[0m\n')

def assertEqual(a, b):
    assert a == b, "\nExpected:\n  %s\nActual:\n  %s\n" % (b, a)
    print('\033[92mPASSED\033[0m\n')

def test_min_by_key():
    example1 = [{'a': 1, 'b': 2}, {'a': 2}]

    example2 = [example1[1], example1[0]]
    example3 = [{}]
    example4 = [{'a': -1}, {'b': -1}]
    example5 = [{'a': 1}, {'b': -1, 'a': 0}]
    example6 = []

    assertEqual(min_by_key('a', example1), example1[0])
    assertEqual(min_by_key('a', example2), example2[1])
    assertEqual(min_by_key('b', example1), example1[1])
    assertEqual(min_by_key('a', example3), example3[0])
    assertEqual(min_by_key('b', example4), example4[1])
    assertEqual(min_by_key('a', example5), example5[1])
    assertEqual(min_by_key('a', example6), -1)

def test_first_by_key():

    example1 = [{'a': 1}]
    example2 = [{'b': 1}, {'b': -2}, {'a': 10}]
    example3 = [{}, {'a': 10, 'b': -10}, {}, {'a': 3, 'c': 3}]

    assertEqual(first_by_key('a', 'asc', example1), example1[0])
    assertIn(first_by_key('a', 'asc', example2), example2[0], example2[1])
    assertEqual(first_by_key('a', 'desc', example2), example2[2])
    assertEqual(first_by_key('b', 'asc', example2), example2[1])
    assertEqual(first_by_key('b', 'desc', example2), example2[0])
    assertEqual(first_by_key('a', 'desc', example3), example3[1])

def main():

    test_min_by_key()
    test_first_by_key()
    test_record_comparator()

if __name__=='__main__':
    main()