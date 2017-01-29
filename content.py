"""
content fixture
"""

CONTENT = """Skip to content
This repository
Search
Pull requests
Issues
Gist
 @niole
 Watch 4,105
  Star 58,591
 Fork 10,637 facebook/react
 Code  Issues 538  Pull requests 106  Projects 0  Wiki  Pulse  Graphs
Tree: 2be0583ed3 Find file Copy pathreact/src/isomorphic/React.js
2be0583  5 days ago
@aweary aweary Update deprecation wording to be less aggressive
5 contributors @zpao @aweary @sebmarkbage @ruiaraujo @spicyj
RawBlameHistory     
106 lines (85 sloc)  2.8 KB
/**
 * Copyright 2013-present, Facebook, Inc.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree. An additional grant
 * of patent rights can be found in the PATENTS file in the same directory.
 *
 * @providesModule React
 */

'use strict';

var ReactChildren = require('ReactChildren');
var ReactComponent = require('ReactComponent');
var ReactPureComponent = require('ReactPureComponent');
var ReactClass = require('ReactClass');
var ReactDOMFactories = require('ReactDOMFactories');
var ReactElement = require('ReactElement');
var ReactPropTypes = require('ReactPropTypes');
var ReactVersion = require('ReactVersion');

var onlyChild = require('onlyChild');
var warning = require('warning');

var createElement = ReactElement.createElement;
var createFactory = ReactElement.createFactory;
var cloneElement = ReactElement.cloneElement;

if (__DEV__) {
  var ReactElementValidator = require('ReactElementValidator');
  createElement = ReactElementValidator.createElement;
  createFactory = ReactElementValidator.createFactory;
  cloneElement = ReactElementValidator.cloneElement;
}

var __spread = Object.assign;
var createMixin = function(mixin) {
  return mixin;
};

if (__DEV__) {
  var warnedForSpread = false;
  var warnedForCreateMixin = false;
  __spread = function() {
    warning(
      warnedForSpread,
      'React.__spread is deprecated and should not be used. Use ' +
      'Object.assign directly or another helper function with similar ' +
      'semantics. You may be seeing this warning due to your compiler. ' +
      'See https://fb.me/react-spread-deprecation for more details.'
    );
    warnedForSpread = true;
    return Object.assign.apply(null, arguments);
  };

  createMixin = function(mixin) {
    warning(
      warnedForCreateMixin,
      'React.createMixin is deprecated and should not be used. You ' +
      'can use this mixin directly instead.'
    );
    warnedForCreateMixin = true;
    return mixin;
  };

}

var React = {

  // Modern

  Children: {
    map: ReactChildren.map,
    forEach: ReactChildren.forEach,
    count: ReactChildren.count,
    toArray: ReactChildren.toArray,
    only: onlyChild,
  },

  Component: ReactComponent,
  PureComponent: ReactPureComponent,

  createElement: createElement,
  cloneElement: cloneElement,
  isValidElement: ReactElement.isValidElement,

  // Classic

  PropTypes: ReactPropTypes,
  createClass: ReactClass.createClass,
  createFactory: createFactory,
  createMixin: createMixin,

  // This looks DOM specific but these are actually isomorphic helpers
  // since they are just generating DOM strings.
  DOM: ReactDOMFactories,

  version: ReactVersion,

  // Deprecated hook for JSX spread, don't use this for anything.
  __spread: __spread,
};

module.exports = React;
Contact GitHub API Training Shop Blog About
2017 GitHub, Inc. Terms Privacy Security Status Help
"""

