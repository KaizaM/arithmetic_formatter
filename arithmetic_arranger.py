def arithmetic_arranger(problems,answer=False):
  operands = ['+','-']
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  
  #check to see if there are less than five math problems
  if len(problems) <= 5:
    for i in problems:
      #take out spaces in string
      i = i.replace(" ", "")
      arithmic = -1
      #check to see whether eqn uses '+' or '-'
      for letter in i:
        if letter in operands:
          arithmic = i.index(letter)
          #check whether we are adding or subtracting
          if letter == '+':
            summation = True
          else:
            summation = False
      
      #if the operation is addition or subtraction
      if arithmic != -1:
        try:
          #get the two numbers
          num1 = int(i[:arithmic])
          num2 = int(i[arithmic+1:])
        #errors if it cannot convert to int (aka not a number)
        except:
          return "Error: Numbers must only contain digits.\n"

        #find the answer to the problem
        if num1 <= 9999 and num2 <= 9999:
          if summation:
            sign = '+'
            sum = num1+num2
          else:
            sign = '-'
            sum = num1-num2

          #this is where the formatting of the equations are done
          #find the size of our strings
          longest_num = max(abs(num1),abs(num2))
          width = len(str(longest_num))+2

          num1_len = len(str(num1))
          num2_len = len(str(num2))
          line = '-'*(width)
          soln_spacing = ' '*(width-len(str(sum)))

          #if the first number is larger
          if num1 == longest_num:
            spacing2 = ' '*(width-num2_len-1)
            line1 += f'  {num1}    '
            line2 += f'{sign}{spacing2}{num2}    '
            line3 += f'{line}    '
            if answer:
              line4 += f'{soln_spacing}{sum}    '

          #if second number is larger
          if num2 == longest_num:
            spacing1 = ' '*(width-num1_len)
            line1 += f'{spacing1}{num1}    '
            line2 += f'{sign} {num2}    '
            line3 += f'{line}    '
            if answer:
              line4 += f'{soln_spacing}{sum}    '
                    
        else:
          return "Error: Numbers cannot be more than four digits.\n"
          break
      else:
        return "Error: Operator must be '+' or '-'\n"
        break
  else:
    return "Error: Too many problems.\n"
    
  final_string = f'{line1}\n{line2}\n{line3}\n{line4}\n'
  return final_string

  
  