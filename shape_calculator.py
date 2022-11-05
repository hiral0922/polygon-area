class Rectangle:
  
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def set_width(self,new_width):
    self.width = new_width
    

  def set_height(self,new_height):
    self.height = new_height
    

  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):
    return ((2 * self.width) + (2 * self.height))

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if (self.width > 50) or (self.height > 50):
      return "Too big for picture."
    else:
      printing_picture = []
      for i in range(self.height):
        lines = "*"*self.width
        printing_picture.append(lines)
      return "\n".join(printing_picture) +"\n"
    
    
    
  def get_amount_inside(self,shape):
    shape_width = shape.width
    shape_height = shape.height
    amount_width = int(self.width / shape.width)
    amount_height = int(self.height / shape.height)
    total_amount = amount_width * amount_height
    return total_amount
       


  def __repr__(self):
    return "Rectangle(width={width}, height={height})".format(width = self.width, height = self.height)
    
class Square(Rectangle):

  def __init__(self,side_length):
    self.width = side_length
    self.height = side_length
    super().set_width(side_length)
    super().set_height(side_length)

  def set_side(self, new_side_length):
    self.width = new_side_length
    self.height = new_side_length

  def __repr__(self):
    return "Square(side={side_length})".format(side_length = self.width)
    

