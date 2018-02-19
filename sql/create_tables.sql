CREATE TABLE buffer_policy
(
  bp_id integer PRIMARY KEY,
  bp_name character varying(40),
  bp_type character varying(40)
);


CREATE TABLE workload
(
  w_id integer PRIMARY KEY,
  w_name character varying(40),
  w_total_of_operations integer,
  read_operations integer,
  write_operations integer,
  unique_pages integer
);


CREATE TABLE test
(
  test_id integer PRIMARY KEY,
  bp_id integer REFERENCES buffer_policy,
  w_id integer REFERENCES workload,
  buffer_size integer,
  write_counter integer,
  hits_counter integer,
  execution_time numeric,
  created_date timestamp without time zone NOT NULL DEFAULT CURRENT_TIMESTAMP
);

