class Solution:
  def ispallidrome(self,x:int)->bool:
    x=str(x)
    reversed_value=x[::-1]
    return x==reversed_value
