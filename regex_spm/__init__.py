import re

from .regex_spm_match import RegexSpmMatch


def search_in(string: str) -> RegexSpmMatch:
  return RegexSpmMatch(string, _match_func=re.search)


def match_in(string: str) -> RegexSpmMatch:
  return RegexSpmMatch(string, _match_func=re.match)


def fullmatch_in(string: str) -> RegexSpmMatch:
  return RegexSpmMatch(string, _match_func=re.fullmatch)


__all__ = ['RegexSpmMatch', 'search_in', 'match_in', 'fullmatch_in']
