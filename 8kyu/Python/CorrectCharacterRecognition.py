'''
Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
The test cases contain numbers only by mistake.
'''
# METHOD 1
def correct(s):
    s = s.replace('5', 'S')
    s = s.replace('0', 'O')
    return s.replace('1', 'I')

# METHOD 2: chain replces together and make lambda
correct = lambda s: s.replace('5', 'S').replace('0', 'O').replace('1', 'I')
