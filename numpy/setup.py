from setuptools import setup

setup(
   name='deepgp_approxep',
   version='1.0',
   description='Approximate Expectation Propagation for Deep GPs',
   author='Thang Bui et al (2016)',
   author_email='thang.buivn@gmail.com',
   packages=['deepgp_approxep'],  #same as name
   install_requires=['numpy'], #external packages as dependencies
)
