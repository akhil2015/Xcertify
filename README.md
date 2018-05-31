# Xcertify
Xcertify is decentralized application built on floblockchain, which can be used to publish certificates, college degrees, results,  and even contact cards. Xcertify makes sure that fake documents cannot be created as they are written over blockchain and verified using digital signatures. 
Currently only CLI version is available , with just the basic certificate templates. I will be releasing the GUI version and 3 more templates in a week or so. Although it already supports user created themes.


You need to run a full flo-qt wallet to run it. Download it from here https://github.com/floblockchain/flo


How to use Xcertify?

-> Download it from github

-> Install htmlmin and webbrowser modules using pip

       pip install htmlmin

       pip install webbrowser

-> You can edit the Xcertify/HTML/index.html according to your need. The attributes should be enclosed  within {{ }} . e.g. {{student_name}}

->Run publish.py. It will automatically detect the attributes and ask you to enter the values.

->if you want to view a document run the view.py file and enter the certificate id and source's address to verify the document. If verification is successful then a browser window with the document should appear.
