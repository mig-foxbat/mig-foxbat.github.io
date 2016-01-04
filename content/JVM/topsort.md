Title: Dag processing
Tags: scala,DAG,sorting
Author: Charles
Summary: Identifying cyclic dependencies in DAG
Date: 2016-01-03

Identifying cyclic dependencies in DAG might sound intimidating but it is quite simple.
In this article I will be showing to do it via Topological sorting. Topological sorting is simply the process of Linearizing a DAG. If Graph is cyclic your Topological sorting will fail (cannot proceed). 


#### How the it works

Lets say you have Graph called `unsorted_graph` as shown in the below image. You now traverse your graph starting with nodes that don't have any dependencies (no incoming edges). In our example these nodes will be Node A and G. Node A and G are removed from `unsorted_graph` and moved to our new target graph `sorted_graph`.  Then again the source graph is queried for free nodes with no dependencies (no incoming edges). This time it will Node B (since Node A is already removed from the graph) and it will placed into the new graph preserving its dependency with A. The process is repeated untill there are no more nodes in your source graph.


![Directed Acyclic Graph](/images/dag/dag.svg)


#### Identify cyclic dependencies

As we walk our source graph identifying free nodes with no dependencies we would go to point sooner or later where there are no more free nodes in the graph before all nodes have been exhausted. We get caught in a classic deadlock scenario where all nodes dependent on someother nodes in the graph and there are no free nodes anymore. 


##### Code snippet

```
case class Node(id: Int, dependencies: List[Node] = List()) {

  def this(id: Int, node: Node) = this(id,List(node))
  
  override def equals(that: Any): Boolean = {
    that match {
      case node: Node => node.id == this.id
      case _ => false
    }
  }

  override def toString = {
    s"$id -> ${(dependencies map {_.id}).mkString(",")}"
  }

}

class Dag(val graph: List[Node]) {

  def sort(): Dag = {
    new Dag(topSort(graph))
  }

  @tailrec
  private def topSort(unsorted_graph: List[Node], sorted_graph: List[Node] = Nil):List[Node] = {
    (unsorted_graph ,sorted_graph) match {
      case (Nil,a) =>  a
      case _ => {
        val open_nodes = unsorted_graph collect {
          case node @ Node(_,Nil) => node
          case node @ Node(_, dependencies) if dependencies forall { sorted_graph contains _ } => node
        }
        if (open_nodes isEmpty) { throw new RuntimeException("Cycles Detected in DAG")}
        topSort(unsorted_graph filterNot { open_nodes contains _  },sorted_graph ++ open_nodes)
      }
    }
  }

  override def toString = {
    this.graph.toString()
  }

}

```

##### Sample Execution

```
    val nodes = Node(1,Nil) :: Node(2,List(Node(1))) :: Node(3,List(Node(1))) :: Node(4,List(Node(2),Node(3))) ::
      Node(6,Nil) :: Node(5,List(Node(4),Node(6))) :: Nil
    val dag = new Dag(nodes) 
    println(dag.sort().toString)
```