print("""Agree to the license:
MIT License

Copyright (c) 2022 Tobey_Source

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

""")
na = input("If you agree type: Y. If you don't then type: N")
if na == "N":
  import os
  os.system("EXIT")
if na == "Y":
  print("Press ENTER to install>>>")
  input()
  with open("C:\Tobey\Sccuz\optionrun.py", "w")as f:
    f.writelines("""
import os
while True:
  openfil = input("Run: ")
  os.startfile(openfil)
    """)
  with open("C:\Tobey\Sccuz\main.py", "w")as f:
    f.writelines("""
print("Sccuzman interface==================1. Run2. cmd3. Make==================")
option = input("<<<Option>>>")
if option == "1":
  import os
  os.startfile("Optionrun.py")
if option == "2":
  import os
  cmd = input("Terminal>")
  os.system(cmd)
if option == "3"
  print("Sccuzman Editor===============Max number of lines: 10 Name:")
  filename = input("")
  print("Ok, ready to edit:", filename)
  print("Write: oksdoijoidjojdojdoixjoijcoidxjojik if you want to finish")
  first_line = input("")
  if first_line == "oksdoijoidjojdojdoixjoijcoidxjojik":
    with open(filename, "w")as f:
      f.writelines()
  else:
    secline = input("")
    if secline == "oksdoijoidjojdojdoixjoijcoidxjojik":
      with open(filename, "w")as f:
        f.writelines(first_line)
    else:
      line3 = input("")
      if line3 == "oksdoijoidjojdojdoixjoijcoidxjojik":
        with open(filename, "w")as f:
          f.writelines(first_line + "\n" + secline + "\n")
      else:
          line4 = input("")
          if line4 == "oksdoijoidjojdojdoixjoijcoidxjojik":
            with open(filename, "w")as f:
              f.writelines(first_line + "\n" + secline + "\n" + line3 + "\n")
          else:
                line5 = input("")
                if line5 == "oksdoijoidjojdojdoixjoijcoidxjojik":
                  with open(filename, "w")as f:
                    f.writelines(first_line + "\n" + secline + "\n" +  line3 + "\n" +  line4 + "\n")
                else:
                  line6 = input("")
                  if line6 == "oksdoijoidjojdojdoixjoijcoidxjojik":
                    with open(filename, "w")as f:
                      f.writelines(first_line + "\n" + secline + "\n" + line3 + "\n" +  line4 + "\n" +  line5 + "\n")
                  else:
                    line7 = input("")
                    if line7 == "oksdoijoidjojdojdoixjoijcoidxjojik":
                      with open(filename, "w")as f:
                        f.writelines(first_line + "\n" + secline + "\n" + line3 + "\n" +  line4 + "\n"+  line5 + "\n" + line6 + "\n")
                    else:
                      line8 = input("")
                      if line8 == "oksdoijoidjojdojdoixjoijcoidxjojik":
                        with open(filename, "w")as f:
                          f.writelines(first_line + "\n" + secline + "\n" + line3 + "\n" +  line4 + "\n" +  line5 + "\n" + line6 + "\n" + line7 + "\n")
                      else:
                        line9 = input("")
                        if line9 == "oksdoijoidjojdojdoixjoijcoidxjojik":
                          with open(filename, "w")as f:
                            f.writelines(first_line + "\n" + secline + "\n" + line3 + "\n" +  line4 + "\n" +  line5 + "\n" + line6 + "\n" + line7 + "\n" + line8 + "\n")
                        else:
                          line10 = input("")
                          if line10 == "oksdoijoidjojdojdoixjoijcoidxjojik":
                            with open(filename, "w")as f:
                              f.writelines(first_line + "\n" + secline + "\n" + line3 + "\n" +  line4 + "\n" +  line5 + "\n" + line6 + "\n" + line7 + "\n" + line8 + "\n" + line9 + "\n")
                          else:
                            with open(filename, "w")as f:
                              f.writelines(first_line + "\n" + secline + "\n" + line3 + "\n" +  line4 + "\n" +  line5 + "\n" + line6 + "\n" + line7 + "\n" + line8 + "\n" + line9 + "\n" + line10 + "\n")
                        
                          
                    
          
      
    """""")
