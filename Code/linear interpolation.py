def interpolate(x1, y1, x2, y2, xin):
  """
  We want to estimate the size between 2 points
  We will use a linear interpolation formula
  """

  formula= (y2-y1)/(x2-x1)*xin + (y1*x2-y2*x1)/(x2-x1)
  return formula


print(interpolate(20,0.05,10,0.1,16))