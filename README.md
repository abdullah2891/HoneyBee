 oneyBee

Example Rule:

```
{
	affectedFiles: [
		{ "conditions": { "all": [
      { "name": "fileExtension",
        "operator": "equal_to",
        "value": 'png',
      },
      { "name": "age",
        "operator": "greater_than",
        "value": 20,
      },
  ]},
  "actions": [
      { "name": "move_to_backup",
        "params": {"directory": 'backup'},
      },
      {
      	"name" : "optical_character_recognition",
	"params": {"directory": 'backup'}
      }
  ],
[
},

	]

}
