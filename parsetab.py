
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'FRACTIONAL_DURATION OCTAVE PITCH REST VOICE WHOLE_DURATIONsong : song voicesong : voicevoice : voice note\n             | voice restvoice : VOICE note\n             | VOICE restnote : FRACTIONAL_DURATION PITCH OCTAVE\n            | WHOLE_DURATION PITCH OCTAVErest : FRACTIONAL_DURATION REST\n            | WHOLE_DURATION REST'
    
_lr_action_items = {'VOICE':([0,1,2,4,5,6,9,10,12,14,15,16,],[3,3,-2,-1,-3,-4,-5,-6,-9,-10,-7,-8,]),'$end':([1,2,4,5,6,9,10,12,14,15,16,],[0,-2,-1,-3,-4,-5,-6,-9,-10,-7,-8,]),'FRACTIONAL_DURATION':([2,3,4,5,6,9,10,12,14,15,16,],[7,7,7,-3,-4,-5,-6,-9,-10,-7,-8,]),'WHOLE_DURATION':([2,3,4,5,6,9,10,12,14,15,16,],[8,8,8,-3,-4,-5,-6,-9,-10,-7,-8,]),'PITCH':([7,8,],[11,13,]),'REST':([7,8,],[12,14,]),'OCTAVE':([11,13,],[15,16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'song':([0,],[1,]),'voice':([0,1,],[2,4,]),'note':([2,3,4,],[5,9,5,]),'rest':([2,3,4,],[6,10,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> song","S'",1,None,None,None),
  ('song -> song voice','song',2,'p_song','parser.py',48),
  ('song -> voice','song',1,'p_song_voice','parser.py',52),
  ('voice -> voice note','voice',2,'p_voice','parser.py',56),
  ('voice -> voice rest','voice',2,'p_voice','parser.py',57),
  ('voice -> VOICE note','voice',2,'p_voice_note','parser.py',63),
  ('voice -> VOICE rest','voice',2,'p_voice_note','parser.py',64),
  ('note -> FRACTIONAL_DURATION PITCH OCTAVE','note',3,'p_note','parser.py',69),
  ('note -> WHOLE_DURATION PITCH OCTAVE','note',3,'p_note','parser.py',70),
  ('rest -> FRACTIONAL_DURATION REST','rest',2,'p_rest','parser.py',74),
  ('rest -> WHOLE_DURATION REST','rest',2,'p_rest','parser.py',75),
]
