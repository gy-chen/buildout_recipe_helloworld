# buildout_recipe_helloworld
This recipe do nothing but record received arguments in a file.
## Install
```sh
git clone https://github.com/gy-chen/buildout_recipe_helloworld.git
cd buildout_recipe_helloworld
pip install zc.buildout
buildout bootstrap
./bin/buildout
```
See the result in parts/hello_recipe
## Try
```sh
./bin/buildout buildout:hello=argument_from_cli
```
See the result in parts/hello_recipe
