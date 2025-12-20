from begin.globals import Crypt, Class
from database import *

import importlib
import inspect

import os
import re

##
class Seeds():
    SEEDS_SEQUENCE = [
        'Room'
        , 'User'
        , 'Predefined'
        # , 'Tst'
    ]

    SEEDS = {}

    SEEDS_PATH = "./begin/globals/Seeds"
    SEEDS_REGEX = "^.*.py$"
    SEEDS_IGNORE = ['__init__.py']

    def __init__(self)->None:
        self.seeds_load()
        print('seeds: ', self.SEEDS)

    def seeds_load(self, folder:str=SEEDS_PATH)->None:
        folder_path = os.path.abspath(folder)

        for file in os.listdir(folder_path):
            file_path = f"{folder_path}/{file}"

            if not os.path.isfile(file_path):
                self.seeds_load(file_path)
                continue

            if not re.search(self.SEEDS_REGEX, file) or file in self.SEEDS_IGNORE:
                continue

            ##
            module_name = file[:-3]
            module_spec = importlib.util.spec_from_file_location(module_name, file_path)

            if not module_spec or not module_spec.loader :
                continue

            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)

            print('module_name: ', module_name)

            ##
            seeds = [
                seed for name, seed in inspect.getmembers(module, inspect.isclass)
                if seed.__module__ == module.__name__
            ]

            self.SEEDS[module_name] = seeds

    def cultivate(self, seed_cultivated:list[str]=[], module_name:str=None, seed_class:object=None)->list[str]:
        print('seed_class2: ', seed_class, seed_cultivated)
        if seed_class and not seed_class.DEPEND_ON :
            return []
        if seed_class and set(seed_class.DEPEND_ON).issubset(set(seed_cultivated)):
            return []

        if seed_class:
            seed_dependencies = seed_class.DEPEND_ON
            dependencies_up = []
            dependencies_all = set(seed_cultivated)
            for dependence_name in seed_dependencies:
                print('seed_class3: ', seed_class, dependencies_all)
                if dependence_name in dependencies_all:
                    continue

                dependence_class = [ obj for obj in self.SEEDS[module_name] if obj.__name__ == dependence_name][0]
                dependencies_up.extend(self.cultivate(list(dependencies_all), module_name, dependence_class))

                _instance = dependence_class()
                dependencies_up.append(dependence_name)

                dependencies_all.update(set(dependencies_up))

            return dependencies_up

        for module_name in self.SEEDS_SEQUENCE:
            seed_cultivated = []
            for seed_class in self.SEEDS[module_name]:
                print('seed_class1: ', seed_class, seed_cultivated)
                seed_cultivated.extend(self.cultivate(seed_cultivated, module_name, seed_class))

                if not seed_class.__name__ in seed_cultivated:
                    seed_instance = seed_class()
                    seed_cultivated.append(seed_class.__name__)
