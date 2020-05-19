from math import ceil
def MergeSort (array):
  if len(array) == 0:
    return([])
  if len(array) == 1:
    return(array)
  mid=ceil(len(array)/2)
  leftarr=array[0:mid]
  rightarr=array[mid:len(array)]

  
  LSorted=MergeSort(leftarr)
  print(LSorted)
  RSorted=MergeSort(rightarr)
  print(RSorted)

  TheAnswer=Sort(LSorted, RSorted)
  print(TheAnswer)
  return(TheAnswer)



def Sort(leftarr, rightarr):
  temp=[]
  i=0
  j=0
  while(i<len(leftarr) and j<len(rightarr)):
    if leftarr[i] <= rightarr[j]:
      temp.append(leftarr[i])
      i += 1
    else:
      temp.append(rightarr[j])
      j += 1

  while(i<len(leftarr)):
     temp.append(leftarr[i])
     i += 1

  while(j<len(rightarr)):
    temp.append(rightarr[j])
    j += 1

  return(temp)
  
class UnitTestObject(object):
  def __init__(self, sort_func):
    self.sort = sort_func

  def test_empty_array(self):
    # use self.sort as tested sort
    empty_array = []
    if (self.sort(empty_array) == []):
      return True
    else:
      return False

  def test_big_same_array(self):
    # use self.sort as tested sort
    array1 = [1,1,1,1,1,1,1,1]
    if (self.sort(array1) == [1,1,1,1,1,1,1,1]):
      return True;
    else:
      return False
  
  def test_reverse(self):
    array=[4000,9,8,7,6,5,4]
    if (self.sort(array)) == [4,5,6,7,8,9,4000]:
      return True
    return False  

  def test_repeats(self):
    array=[5,47,5,47,3,2]
    if (self.sort(array) == [2,3,5,5,47,47]):
      return True
    return False   
  #etc


#main script


#sorted_array = sort(my_array)

unit_tests = UnitTestObject(MergeSort)

print(unit_tests.test_empty_array())
print(unit_tests.test_big_same_array())
print(unit_tests.test_reverse())
print(unit_tests.test_repeats()) 
