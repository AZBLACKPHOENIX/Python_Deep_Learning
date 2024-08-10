import tensorflow as tf

# Disable eager execution to use graph mode
tf.compat.v1.disable_eager_execution()

# Get the default graph
graph = tf.compat.v1.get_default_graph()

# Get the list of operations in the graph
operations = graph.get_operations()


#Declare variables
a = tf.constant(10,  name="a")
b = tf.constant(20, name="b")
#Create operations
c = tf.add(a,b, name="c")
d=tf.multiply(a,c, name="d")
e=tf.multiply(d,c, name="e")

sess = tf.compat.v1.Session()

#Print operations
for op in graph.get_operations():
    print(op)
