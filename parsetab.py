
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expressionleftORleftANDleftLPARENRPARENrightNOTleftISNAME VALUE IS AND OR LBRACKET RBRACKET LPAREN RPAREN NOT OPTION ATLEASTONE ANYexpression : quantifiedstep \n                  | quantifiedstep expressionquantifiedstep : step \n            | OPTION step\n            | ATLEASTONE step \n            | ANY stepstep : atomicconstraint\n            | NOT step\n            | LBRACKET classconstraint RBRACKET classconstraint : partofclassconstraint \n            | partofclassconstraint AND classconstraint\n            | partofclassconstraint OR classconstraint partofclassconstraint : atomicconstraint\n                    | LPAREN classconstraint RPAREN  \n                    | NOT classconstraint atomicconstraint : NAME IS VALUE '
    
_lr_action_items = {'LPAREN':([7,16,17,26,27,],[16,16,16,16,16,]),'AND':([15,19,22,24,28,29,30,],[-13,26,-16,-15,-14,-11,-12,]),'RPAREN':([15,19,22,23,24,28,29,30,],[-13,-10,-16,28,-15,-14,-11,-12,]),'VALUE':([14,],[22,]),'OPTION':([0,1,8,9,11,12,13,21,22,25,],[3,-7,3,-3,-5,-4,-6,-8,-16,-9,]),'ATLEASTONE':([0,1,8,9,11,12,13,21,22,25,],[2,-7,2,-3,-5,-4,-6,-8,-16,-9,]),'ANY':([0,1,8,9,11,12,13,21,22,25,],[4,-7,4,-3,-5,-4,-6,-8,-16,-9,]),'NAME':([0,1,2,3,4,7,8,9,10,11,12,13,16,17,21,22,25,26,27,],[5,-7,5,5,5,5,5,-3,5,-5,-4,-6,5,5,-8,-16,-9,5,5,]),'RBRACKET':([15,18,19,22,24,28,29,30,],[-13,25,-10,-16,-15,-14,-11,-12,]),'NOT':([0,1,2,3,4,7,8,9,10,11,12,13,16,17,21,22,25,26,27,],[10,-7,10,10,10,17,10,-3,10,-5,-4,-6,17,17,-8,-16,-9,17,17,]),'IS':([5,],[14,]),'LBRACKET':([0,1,2,3,4,8,9,10,11,12,13,21,22,25,],[7,-7,7,7,7,7,-3,7,-5,-4,-6,-8,-16,-9,]),'$end':([1,6,8,9,11,12,13,20,21,22,25,],[-7,0,-1,-3,-5,-4,-6,-2,-8,-16,-9,]),'OR':([15,19,22,24,28,29,30,],[-13,27,-16,-15,-14,-11,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'atomicconstraint':([0,2,3,4,7,8,10,16,17,26,27,],[1,1,1,1,15,1,1,15,15,15,15,]),'expression':([0,8,],[6,20,]),'classconstraint':([7,16,17,26,27,],[18,23,24,29,30,]),'partofclassconstraint':([7,16,17,26,27,],[19,19,19,19,19,]),'step':([0,2,3,4,8,10,],[9,11,12,13,9,21,]),'quantifiedstep':([0,8,],[8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> quantifiedstep','expression',1,'p_expression','pyrata_parser.py',38),
  ('expression -> quantifiedstep expression','expression',2,'p_expression','pyrata_parser.py',39),
  ('quantifiedstep -> step','quantifiedstep',1,'p_quantifiedstep','pyrata_parser.py',98),
  ('quantifiedstep -> OPTION step','quantifiedstep',2,'p_quantifiedstep','pyrata_parser.py',99),
  ('quantifiedstep -> ATLEASTONE step','quantifiedstep',2,'p_quantifiedstep','pyrata_parser.py',100),
  ('quantifiedstep -> ANY step','quantifiedstep',2,'p_quantifiedstep','pyrata_parser.py',101),
  ('step -> atomicconstraint','step',1,'p_step','pyrata_parser.py',229),
  ('step -> NOT step','step',2,'p_step','pyrata_parser.py',230),
  ('step -> LBRACKET classconstraint RBRACKET','step',3,'p_step','pyrata_parser.py',231),
  ('classconstraint -> partofclassconstraint','classconstraint',1,'p_classconstraint','pyrata_parser.py',293),
  ('classconstraint -> partofclassconstraint AND classconstraint','classconstraint',3,'p_classconstraint','pyrata_parser.py',294),
  ('classconstraint -> partofclassconstraint OR classconstraint','classconstraint',3,'p_classconstraint','pyrata_parser.py',295),
  ('partofclassconstraint -> atomicconstraint','partofclassconstraint',1,'p_partofclassconstraint','pyrata_parser.py',316),
  ('partofclassconstraint -> LPAREN classconstraint RPAREN','partofclassconstraint',3,'p_partofclassconstraint','pyrata_parser.py',317),
  ('partofclassconstraint -> NOT classconstraint','partofclassconstraint',2,'p_partofclassconstraint','pyrata_parser.py',318),
  ('atomicconstraint -> NAME IS VALUE','atomicconstraint',3,'p_atomicconstraint','pyrata_parser.py',338),
]
