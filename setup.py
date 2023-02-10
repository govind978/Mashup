from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'Govind-Singla-102016060',
  packages = ['Govind-Singla-102016060'],
  version = '0.0.1',      
  license='MIT',        
  description = 'This module will create a mashup sort of thing of any singer you want of any duration with just simple command.',
  long_description=long_description,
  long_description_content_type='text/markdown',   
  author = 'Govind Singla',                   
  author_email = 'singlagovind794@gmail.com',      
  keywords = ['MASHUP', 'YOUTUBE', 'PROJECT','MUSIC','MP3'],   
  install_requires=[           
          'pytube',
          'pydub',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
