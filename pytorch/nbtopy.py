import sys,json,os

_dir = os.path.join(os.getcwd(),"pytorch")
_input = os.path.join(_dir,"dqn.ipynb")
_output =  os.path.join(_dir,"dqn_export.py")

print("input={0} output={1}".format(_input,_output))

f = open(_input, 'r') #input.ipynb
j = json.load(f)
of = open(_output, 'w') #output.py
if j["nbformat"] >=4:
        for i,cell in enumerate(j["cells"]):
                of.write("#cell "+str(i)+"\n")
                for line in cell["source"]:
                        of.write(line)
                of.write('\n\n')
else:
        for i,cell in enumerate(j["worksheets"][0]["cells"]):
                of.write("#cell "+str(i)+"\n")
                for line in cell["input"]:
                        of.write(line)
                of.write('\n\n')

of.close()

print("finished")