import re
from abc import ABC

import regex_spm


class MyRegexes(ABC):
    letters = re.compile(r'[a-zA-Z]+')
    numbers = r'[0-9]+'


class TestSpmSearch:
    def test_spm_search_scenario_1(self):
        match regex_spm.search_in('abcdef'):
            case MyRegexes.numbers:
                assert False
            case MyRegexes.letters:
                assert True
            case _:
                assert False
    
    def test_spm_search_scenario_2(self):
        match regex_spm.search_in('abcd12345ef'):
            case MyRegexes.numbers as m:
                assert m[0] == '12345'
            case _:
                assert False
    
    def test_spm_search_scenario_3(self):
        match regex_spm.search_in('abcdededef'):
            case r'(de)+' as m:
                assert m[0] == 'dedede'
                assert m.match[1] == 'de'
            case _:
                assert False


class TestSpmMatch:
    def test_spm_match_scenario_1(self):
        match regex_spm.match_in('abcdef'):
            case MyRegexes.numbers:
                assert False
            case MyRegexes.letters:
                assert True
            case _:
                assert False
    
    def test_spm_match_scenario_2(self):
        match regex_spm.match_in('abcd12345'):
            case MyRegexes.numbers:
                assert False
            case MyRegexes.letters as m:
                assert m[0] == 'abcd'
            case _:
                assert False
    
    def test_spm_match_scenario_3(self):
        match regex_spm.match_in('abcdededef'):
            case r'abc(de)+' as m:
                assert m[0] == 'abcdedede'
                assert m.match[1] == 'de'
            case _:
                assert False


class TestSpmFullMatch:
    def test_spm_fullmatch_scenario_1(self):
        match regex_spm.fullmatch_in('abcdef'):
            case MyRegexes.numbers:
                assert False
            case MyRegexes.letters as m:
                assert m[0] == 'abcdef'
            case _:
                assert False
    
    def test_spm_fullmatch_scenario_2(self):
        match regex_spm.fullmatch_in('abcd12345'):
            case MyRegexes.numbers:
                assert False
            case MyRegexes.letters:
                assert False
            case '[a-z]+[0-9]+':
                assert True
            case _:
                assert False
    
    def test_spm_fullmatch_scenario_3(self):
        match regex_spm.fullmatch_in('abcdededef'):
            case r'abc(de)+f' as m:
                assert m[0] == 'abcdededef'
                assert m.match[1] == 'de'
            case _:
                assert False
