SELECT_SCMBP_FAMILY =  "select bp_id, bp_name from buffer_policy where bp_type =%s " %("'SCMBP FAMILY BUFFER POLICIES'")

SELECT_NON_SCM_AWARE = "select bp_id, bp_name from buffer_policy where bp_type =%s" %("'NON SCM-AWARE BUFFER POLICIES'")

SELECT_SCM_AWARE = "select bp_id, bp_name from buffer_policy where bp_type =%s" %("'SCM-AWARE BUFFER POLICIES'")

SELECT_WORKLOAD = 'select w_id, w_name from workload'

SELECT_TEST     = 'select hits_counter, write_counter from test where bp_id=%i and w_id=%i and buffer_size=%i'

SELECT_BUFFER_SIZE     = 'select distinct buffer_size from test order by 1'