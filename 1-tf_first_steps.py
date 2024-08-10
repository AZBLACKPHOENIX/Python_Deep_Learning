import tensorflow as tf

#declare variables
zero=tf.Variable(0)
three = tf.Variable(3)
#declare constant
one=tf.constant(1)
#add values
new_var = tf.add(zero, one)
#update variable
update=tf.assign(zero, new_var)

#inintialize variables
init_op = tf.global_variables_initializer()

with tf.Session() as s:
    s.run(init_op)
    for _ in range(5):
        s.run(update)
        print(s.run(zero))