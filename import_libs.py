import requests
from bs4 import BeautifulSoup, Tag, NavigableString as NS
import bs4
from typing import Tuple, Union, List
import re
from flask import Flask, jsonify, request 