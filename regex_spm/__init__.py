import re

from regex_spm_match import RegexSpmMatch


def search(string: str) -> RegexSpmMatch:
  return RegexSpmMatch(string, _match_func=re.search)


def match(string: str) -> RegexSpmMatch:
  return RegexSpmMatch(string, _match_func=re.match)


def fullmatch(string: str) -> RegexSpmMatch:
  return RegexSpmMatch(string, _match_func=re.fullmatch)


__all__ = ['RegexSpmMatch', 'search', 'match', 'fullmatch']