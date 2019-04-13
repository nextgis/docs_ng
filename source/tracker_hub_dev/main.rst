.. sectionauthor:: Дмитрий Барышников <dmitry.baryshnikov@nextgis.ru>
.. NextGIS tracker hub ащк developer

NextGIS Tracker hub for developers
=====================================

The endpoint for tracker API is ``track.nextgis.com``.

Send location packet
---------------------

To send track points to NextGIS tracker hub execute following request:

.. http:post:: /ng-mobile/(string:guid)/packet

   Post track points request

   :param guid: tracker identifier
   :reqheader Accept: must be ``*/*``
   :<jsonarr: track points array
   :<json double lt: latitude of track point
   :<json double ln: longitude of track point
   :<json int ts: timestamp
   :<json double a: elevation of track point
   :<json int s: satellite count used in fix
   :<json string ft: fix type [2d, 3d ...]
   :<json double sp: speed
   :<json double ha: accuracy
   :statuscode 200: no error

**Example request**:

.. sourcecode:: http

   POST /ng-mobile/971f1-ffc-0f7073/packet HTTP/1.1
   Host: track.nextgis.com
   Accept: */*

   [
    {
        "lt": 0.000044915764204969081,
        "ln": 0.000044915764205976054,
        "ts": 1553418558,
        "a": 5,
        "s": 5,
        "ft": 3,
        "sp": 18,
        "ha": 5
    },
    {
        "lt": 0.000053898917045962894,
        "ln": 0.000053898917047171271,
        "ts": 1553418559,
        "a": 6,
        "s": 6,
        "ft": 3,
        "sp": 21.6,
        "ha": 6
    },
    {
        "lt": 0.000062882069886956708,
        "ln": 0.000062882069888366482,
        "ts": 1553418561,
        "a": 7,
        "s": 7,
        "ft": 3,
        "sp": 25.2,
        "ha": 7
    }
   ]

Check tracker is registered at tracker hub
-------------------------------------------

To check if tracker is registered at NextGIS tracker hub execute following request:

.. http:post:: /ng-mobile/(string:guid)/registered

   Check if tracker is registered request

   :param guid: tracker identifier
   :reqheader Accept: must be ``*/*``
   :statuscode 200: no error

**Example request**:

If registered at NextGIS tracker hub:

.. sourcecode:: http

   POST /ng-mobile/971f1-ffc-0f7073/registered HTTP/1.1
   Host: track.nextgis.com
   Accept: */*

   {"registered": true}

If not registered at NextGIS tracker hub:

.. sourcecode:: http

   POST /ng-mobile/971f1-ffc-0f7073/registered HTTP/1.1
   Host: track.nextgis.com
   Accept: */*

   {"registered": false}

Get track points
----------------

Short output 1
^^^^^^^^^^^^^^

To get track points from NextGIS Web execute following request:

.. http:get:: /tracker/tracks/short?devices_id=(int:id1),(int:id2)&date_time_from=(string: ISO timestamp)&date_time_to=(string: ISO timestamp)

   Post track points request

   :param guid: tracker identifier
   :reqheader Accept: must be ``*/*``
   :statuscode 200: no error

**Example request**:

.. sourcecode:: http

   GET /tracker/tracks/short?devices_id=14,23&date_time_from=2019-04-01T10:00:00.000Z&date_time_to=2019-04-01T15:00:00.000Z HTTP/1.1
   Host: demo.nextgis.com
   Accept: */*

   {
    "14": [
        [
            {
                "lat": 52.08881305,
                "h": 146,
                "lon": 23.70545869
            },
            {
                "lat": 52.08897581,
                "h": 169,
                "lon": 23.70549827
            },
            {
                "lat": 52.08914306,
                "h": 194,
                "lon": 23.70550141
            }
        ],
        [
            {
                "lat": 52.09576269,
                "h": 194,
                "lon": 23.73853582
            },
            {
                "lat": 52.09564859,
                "h": 181,
                "lon": 23.73879119
            },
            {
                "lat": 52.09555082,
                "h": 174,
                "lon": 23.73889233
            }
        ],
        [
            {
                "lat": 52.09650613,
                "h": 160,
                "lon": 23.74376705
            },
            {
                "lat": 52.09658299,
                "h": 165,
                "lon": 23.74365873
            },
            {
                "lat": 52.09664014,
                "h": 166,
                "lon": 23.74351429
            }
        ],
        [
            {
                "lat": 52.09682634,
                "h": 151,
                "lon": 23.74517907
            },
            {
                "lat": 52.09671756,
                "h": 172,
                "lon": 23.74514079
            },
            {
                "lat": 52.09661784,
                "h": 168,
                "lon": 23.74519602
            }
        ]
    ],
    "23": []
  }


Short output 2
^^^^^^^^^^^^^^

To get track points from NextGIS Web execute following request:

.. http:get:: /tracker/tracks/short?devices_id=(int:id1),(int:id2)&date_time_from=(string: ISO timestamp)&date_time_to=(string: ISO timestamp)&array&srs=(int:srs)

   Post track points request

   :param guid: tracker identifier
   :reqheader Accept: must be ``*/*``
   :statuscode 200: no error

**Example request**:

.. sourcecode:: http

   GET /tracker/tracks/short?devices_id=14,23&date_time_from=2019-04-01T10:00:00.000Z&date_time_to=2019-04-01T15:00:00.000Z HTTP/1.1
   Host: demo.nextgis.com
   Accept: */*

   {
    "14": [
        [
            [
                3270299.2317780224,
                7596000.373302298,
                146
            ],
            [
                3270285.911302843,
                7595988.225716175,
                169
            ],
            [
                3270274.2602909105,
                7595974.103075141,
                194
            ]
        ],
        [
            [
                3267691.9639889407,
                7597017.3687444,
                160
            ],
            [
                3267692.5723902555,
                7597006.083770043,
                165
            ],
            [
                3267696.4936128575,
                7596994.903371635,
                166
            ]
        ]
    ],
    "23": []
  }

Full output
^^^^^^^^^^^^

To get track points from NextGIS Web execute following request:

.. http:get:: /tracker/tracks/full?devices_id=(int:id1),(int:id2)&date_time_from=(string: ISO timestamp)&date_time_to=(string: ISO timestamp)

   Post track points request

   :param guid: tracker identifier
   :reqheader Accept: must be ``*/*``
   :statuscode 200: no error

**Example request**:

.. sourcecode:: http

   GET /tracker/tracks/full?devices_id=14,23&date_time_from=2019-04-01T10:00:00.000Z&date_time_to=2019-04-01T15:00:00.000Z HTTP/1.1
   Host: demo.nextgis.com
   Accept: */*

   {
       "14": [
           [
               {
                   "lat": 52.08881305,
                   "h": 146,
                   "lon": 23.70545869,
                   "packet": {
                       "c": null,
                       "sat_gp": 11,
                       "did": 14,
                       "s": 0,
                       "t": "2019-04-01T13:05:57+00:00",
                       "sat_gl": null
                   }
               },
               {
                   "lat": 52.08897581,
                   "h": 169,
                   "lon": 23.70549827,
                   "packet": {
                       "c": null,
                       "sat_gp": 16,
                       "did": 14,
                       "s": 0,
                       "t": "2019-04-01T13:05:59+00:00",
                       "sat_gl": null
                   }
               },
               {
                   "lat": 52.08914306,
                   "h": 194,
                   "lon": 23.70550141,
                   "packet": {
                       "c": null,
                       "sat_gp": 16,
                       "did": 14,
                       "s": 0,
                       "t": "2019-04-01T13:06:01+00:00",
                       "sat_gl": null
                   }
               }
           ],
           [
               {
                   "lat": 52.09637467,
                   "h": 162,
                   "lon": 23.74533841,
                   "packet": {
                       "c": null,
                       "sat_gp": 13,
                       "did": 14,
                       "s": 0,
                       "t": "2019-04-01T17:27:01+00:00",
                       "sat_gl": null
                   }
               },
               {
                   "lat": 52.09631452,
                   "h": 160,
                   "lon": 23.7454654,
                   "packet": {
                       "c": null,
                       "sat_gp": 16,
                       "did": 14,
                       "s": 3.7439998626708983,
                       "t": "2019-04-01T17:28:07+00:00",
                       "sat_gl": null
                   }
               },
               {
                   "lat": 52.09634283,
                   "h": 162,
                   "lon": 23.74561459,
                   "packet": {
                       "c": null,
                       "sat_gp": 18,
                       "did": 14,
                       "s": 3.312000060081482,
                       "t": "2019-04-01T17:28:33+00:00",
                       "sat_gl": null
                   }
               }
           ]
       ],
       "23": []
   }
