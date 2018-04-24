#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime
import os

AUTHOR = u'The OpenRA Authors'
SITENAME = u'OpenRA'
SITEURL = 'http://www.openra.net'

DOWNLOAD_GITHUB_BASE_PATH = "https://github.com/OpenRA/OpenRA/"

# Disable if you're doing something that may hit the gh rate limit (60 queries per hour for non-authenticated users)
ENABLE_GITHUB_API = True

# Github release IDs: obtain from https://api.github.com/repos/OpenRA/OpenRA/releases
GITHUB_PLAYTEST_ID = ''
GITHUB_RELEASE_ID = '9988848'

PATH = 'content'
STATIC_PATHS = ['images', 'pages', 'scripts']
HOME_IMAGES = [file for file in os.listdir('./content/images/screenshots/') if file.endswith('.png')]

DIRECT_TEMPLATES = ['index', 'news', 'download', 'games', 'players', 'authors', 'categories', 'tags']

TIMEZONE = 'Europe/Berlin'
NOW = datetime.datetime.utcnow().year

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
# TODO
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# TODO
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

SOCIAL = ([u"Facebook", u"facebook", u"https://www.facebook.com/openra"],
          [u"Twitter", u"twitter", u"http://twitter.com/openRA"],
          [u"Reddit", u"reddit", u"http://www.reddit.com/r/openra"],
          [u"Youtube", u"youtube", u"https://www.youtube.com/channel/UCRoiPL1J4K1-EhQeNazrYig"],
          [u"Google+", u"gplus", u"https://www.google.com/+OpenraNet"],
          [u"Steam", u"steam", u"http://steamcommunity.com/groups/openra/"],
          [u"itch.io", u"itchio", u"https://openra.itch.io/openra"],
          [u"GameReplays", u"gamereplays", u"http://www.gamereplays.org/openra/"],
          [u"Github", u"github", u"https://github.com/OpenRA/OpenRA"],
          [u"ModDB", u"moddb", u"http://www.moddb.com/games/openra"])

PLATFORMS = {u"win":u"Windows",
             u"osx":u"OS X",
             u"deb":u"Debian / Ubuntu",
             u"rpm":u"Fedora / openSUSE",
             u"arch":u"Arch Linux",
             u"gentoo":u"Gentoo",
             u"exherbo":u"Exherbo",
             u"freebsd":u"FreeBSD"}

PLAYTEST_TAG = "test"#fetch_git_tag(GITHUB_PLAYTEST_ID)
RELEASE_TAG = "release"#fetch_git_tag(GITHUB_RELEASE_ID)
playtest_tag = "yoo"
SIZES = "size"#fetch_package_sizes([GITHUB_RELEASE_ID, GITHUB_PLAYTEST_ID])

# TODO, see games.html, players.html
DEBUG = False
SCRIPTS = [file for file in os.listdir('./content/scripts/') if file.endswith('.js')]

DEFAULT_PAGINATION = False

def package_name(platform, tag):
  modtag = tag.gsub('-', '.')
  if platform == "osx":
#    if tag == "release-20170527": return "OpenRA-#{tag}.zip"
    return "OpenRA-#{tag}.dmg"

  if platform == "win":
    return "OpenRA-#{tag}.exe"

  if platform == "deb":
    return "openra_#{modtag}_all.deb"

  raise "Why is your platform #{platform}?!?!"
  return

def generate_download_button(platform, github_id, tag, sizes):
  if github_id == "":
    return "<span>No playtest available<br />(release is newer)</span>"
  elif platform == "source":
    url = DOWNLOAD_GITHUB_BASE_PATH + "archive/#{tag}.tar.gz"
    return "yo" #sprintf('<a href="%s" title=\"Download %s">Download %s<br />(source package)</a>', url, tag, tag)
  else:
    package = package_name(platform, tag)
    url = DOWNLOAD_GITHUB_BASE_PATH + "releases/download/" + tag + '/' + package
    size = sprintf("(%.2f MB)", sizes[package] / 1048576.0) if package in sizes else "(size unknown)"
    return "yo" #sprintf('<a href="%s" title="Download %s">Download %s<br />%s</a>', url, tag, tag, size)

  return "xyz"

def fetch_package_sizes(gh_release_ids):
#  require 'octokit'
  s = Hash.new
  if ENABLE_GITHUB_API:
    if "GITHUB_OAUTH" in ENV:
      Octokit.access_token = ENV['GITHUB_OAUTH']
    for id in gh_release_ids.each:
      if id == "":
        continue
      assets = Octokit.release_assets('https://api.github.com/repos/OpenRA/OpenRA/releases/' + id)
      for asset in assets:
        s[asset.name] = asset.size

  return s

def fetch_git_tag(github_id):
#  require 'octokit'
  if ENABLE_GITHUB_API and github_id != '':
    if "GITHUB_OAUTH" in ENV:
      Octokit.access_token = ENV['GITHUB_OAUTH']

    asset = Octokit.release_asset('https://api.github.com/repos/OpenRA/OpenRA/releases/' + github_id)
    asset.tag_name

  return "unknown-12345678"

def fetch_git_tags():
#  require 'octokit'
  if ENABLE_GITHUB_API:
    if "GITHUB_OAUTH" in ENV:
     Octokit.access_token = ENV['GITHUB_OAUTH']
#    return Octokit.releases('OpenRA/OpenRA').map {|release| release.tag_name} #todo
  return []

def pretty_date(date):
  return attribute_to_time(date).strftime("%Y-%m-%d")

def navigation_page(page):
#  return page == @item.path || (page == "/news/" && @item.path.start_with?("/news/")) #todo
  return

# TODO ?
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
