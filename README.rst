Small library extracted from pip code to easily install wheel files programatically


from cric import install_wheel

scheme = {
    'lib': '/some/path',
    'platlib': '/some/path',
}

install_wheel('/home/user/pip-9.0.1-py2.py3-any-none.whl', scheme)
