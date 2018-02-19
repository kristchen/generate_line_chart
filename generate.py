import pygal
import selects
import confs

def getChartLine(title, labels, work, columns):
	
	line_chart = pygal.Line(human_readable=True, width=1800, height=800)
	line_chart.title = ('%s | %s') %(work[1], title)
	line_chart.x_labels = labels
	line_chart.x_title  = 'Database Buffer Size (Pages)'
	line_chart.y_title  = title
	line_chart.legend_at_bottom = True 
	line_chart.legend_at_bottom_columns = columns
	
	return line_chart

def generateChart(workload, buffers, politicas, labels, filename):

	for work in workload:

		lineHITS = getChartLine('Hit Counter', labels, work, len(politicas))
		lineWRITES = getChartLine('Write Counter', labels, work, len(politicas))
		
		for politica in politicas:
			hits = []
			writes = []
			for size in buffers:
				cursor.execute(selects.SELECT_TEST %(politica[0], work[0], size[0]))
				test = cursor.fetchall()
				writes.append(test[0][1])
				hits.append(test[0][0])

			lineHITS.add(politica[1], hits)
			lineWRITES.add(politica[1], writes)

		# Para cada carga de trabalho eh gerado o grafico de hits e writes
		lineHITS.render_to_png(filename+"-"+work[1].lower()+"-hit-"+'.png')
		lineWRITES.render_to_png(filename+"-"+work[1].lower()+"-write-"+'.png')


if __name__ == '__main__':
	cursor = confs.get_conn()

	cursor.execute(selects.SELECT_WORKLOAD)
	workload = cursor.fetchall()

	cursor.execute(selects.SELECT_BUFFER_SIZE)
	buffers = cursor.fetchall()
	labels = [size[0] for size in buffers]

# --------Select politicas ----------------
	cursor.execute(selects.SELECT_SCMBP_FAMILY)
	scmbp = cursor.fetchall()

	cursor.execute(selects.SELECT_NON_SCM_AWARE)
	no_scm = cursor.fetchall()

	cursor.execute(selects.SELECT_SCM_AWARE)
	scm = cursor.fetchall()
# ------------------------------------------
	politicas = scmbp + no_scm
	generateChart(workload, buffers, politicas, labels, 'scmbp-noscm')

	politicas = scmbp + scm
	generateChart(workload, buffers, politicas, labels, 'scmbp-scm')







