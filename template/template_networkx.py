# ***** Processed with utils_docstring_cleanup.py ******
"""
License:
https://raw.githubusercontent.com/networkx/networkx/master/LICENSE.txt
"""
"""
Views of core data structures such as nested Mappings (e.g. dict-of-dicts).
These ``Views`` often restrict element access, with either the entire view or
layers of nested mappings being read-only.
"""
import warnings
from collections.abc import Mapping
__all__ = ['AtlasView', 'AdjacencyView', 'MultiAdjacencyView', 'UnionAtlas',
    'UnionAdjacency', 'UnionMultiInner', 'UnionMultiAdjacency',
    'FilterAtlas', 'FilterAdjacency', 'FilterMultiInner',
    'FilterMultiAdjacency']


class AtlasView(Mapping):
    __slots__ = '_atlas',

    def __getstate__(self):
        return {'_atlas': self._atlas}

    def __setstate__(self, state):
        self._atlas = state['_atlas']

    def __init__(self, d):
        self._atlas = d

    def __len__(self):
        return len(self._atlas)

    def __iter__(self):
        return iter(self._atlas)

    def __getitem__(self, key):
        return self._atlas[key]

    def copy(self):
        return {n: self[n].copy() for n in self._atlas}

    def __str__(self):
        return str(self._atlas)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._atlas!r})'


class AdjacencyView(AtlasView):
    __slots__ = ()

    def __getitem__(self, name):
        return AtlasView(self._atlas[name])

    def copy(self):
        return {n: self[n].copy() for n in self._atlas}


"""
View Classes provide node, edge and degree "views" of a graph.
Views for nodes, edges and degree are provided for all base graph classes.
A view means a read-only object that is quick to create, automatically
updated when the graph changes, and provides basic access like `n in V`,
`for n in V`, `V[n]` and sometimes set operations.
The views are read-only iterable containers that are updated as the
graph is updated. As with dicts, the graph should not be updated
while iterating through the view. Views can be iterated multiple times.
Edge and Node views also allow data attribute lookup.
The resulting attribute dict is writable as `G.edges[3, 4]['color']='red'`
Degree views allow lookup of degree values for single nodes.
Weighted degree is supported with the `weight` argument.
NodeView
========
    `V = G.nodes` (or `V = G.nodes()`) allows `len(V)`, `n in V`, set
    operations e.g. "G.nodes & H.nodes", and `dd = G.nodes[n]`, where
    `dd` is the node data dict. Iteration is over the nodes by default.
NodeDataView
============
    To iterate over (node, data) pairs, use arguments to `G.nodes()`
    to create a DataView e.g. `DV = G.nodes(data='color', default='red')`.
    The DataView iterates as `for n, color in DV` and allows
    `(n, 'red') in DV`. Using `DV = G.nodes(data=True)`, the DataViews
    use the full datadict in writeable form also allowing contain testing as
    `(n, {'color': 'red'}) in VD`. DataViews allow set operations when
    data attributes are hashable.
DegreeView
==========
    `V = G.degree` allows iteration over (node, degree) pairs as well
    as lookup: `deg=V[n]`. There are many flavors of DegreeView
    for In/Out/Directed/Multi. For Directed Graphs, `G.degree`
    counts both in and out going edges. `G.out_degree` and
    `G.in_degree` count only specific directions.
    Weighted degree using edge data attributes is provide via
    `V = G.degree(weight='attr_name')` where any string with the
    attribute name can be used. `weight=None` is the default.
    No set operations are implemented for degrees, use NodeView.
    The argument `nbunch` restricts iteration to nodes in nbunch.
    The DegreeView can still lookup any node even if nbunch is specified.
EdgeView
========
    `V = G.edges` or `V = G.edges()` allows iteration over edges as well as
    `e in V`, set operations and edge data lookup `dd = G.edges[2, 3]`.
    Iteration is over 2-tuples `(u, v)` for Graph/DiGraph. For multigraphs
    edges 3-tuples `(u, v, key)` are the default but 2-tuples can be obtained
    via `V = G.edges(keys=False)`.
    Set operations for directed graphs treat the edges as a set of 2-tuples.
    For undirected graphs, 2-tuples are not a unique representation of edges.
    So long as the set being compared to contains unique representations
    of its edges, the set operations will act as expected. If the other
    set contains both `(0, 1)` and `(1, 0)` however, the result of set
    operations may contain both representations of the same edge.
EdgeDataView
============
    Edge data can be reported using an EdgeDataView typically created
    by calling an EdgeView: `DV = G.edges(data='weight', default=1)`.
    The EdgeDataView allows iteration over edge tuples, membership checking
    but no set operations.
    Iteration depends on `data` and `default` and for multigraph `keys`
    If `data is False` (the default) then iterate over 2-tuples `(u, v)`.
    If `data is True` iterate over 3-tuples `(u, v, datadict)`.
    Otherwise iterate over `(u, v, datadict.get(data, default))`.
    For Multigraphs, if `keys is True`, replace `u, v` with `u, v, key`
    to create 3-tuples and 4-tuples.
    The argument `nbunch` restricts edges to those incident to nodes in nbunch.
"""
from collections.abc import Mapping, Set
__all__ = ['NodeView', 'NodeDataView', 'EdgeView', 'OutEdgeView',
    'InEdgeView', 'EdgeDataView', 'OutEdgeDataView', 'InEdgeDataView',
    'MultiEdgeView', 'OutMultiEdgeView', 'InMultiEdgeView',
    'MultiEdgeDataView', 'OutMultiEdgeDataView', 'InMultiEdgeDataView',
    'DegreeView', 'DiDegreeView', 'InDegreeView', 'OutDegreeView',
    'MultiDegreeView', 'DiMultiDegreeView', 'InMultiDegreeView',
    'OutMultiDegreeView']


class NodeView(Mapping, Set):
    __slots__ = '_nodes',

    def __getstate__(self):
        return {'_nodes': self._nodes}

    def __setstate__(self, state):
        self._nodes = state['_nodes']

    def __init__(self, graph):
        self._nodes = graph._node

    def __len__(self):
        return len(self._nodes)

    def __iter__(self):
        return iter(self._nodes)

    def __getitem__(self, n):
        if isinstance(n, slice):
            raise nx.NetworkXError(
                f'{type(self).__name__} does not support slicing, try list(G.nodes)[{n.start}:{n.stop}:{n.step}]'
                )
        return self._nodes[n]

    def __contains__(self, n):
        return n in self._nodes

    @classmethod
    def _from_iterable(cls, it):
        return set(it)

    def __call__(self, data=False, default=None):
        if data is False:
            return self
        return NodeDataView(self._nodes, data, default)

    def data(self, data=True, default=None):
        if data is False:
            return self
        return NodeDataView(self._nodes, data, default)

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return f'{self.__class__.__name__}({tuple(self)})'


class OutEdgeDataView:
    __slots__ = ('_viewer', '_nbunch', '_data', '_default', '_adjdict',
        '_nodes_nbrs', '_report')

    def __getstate__(self):
        return {'viewer': self._viewer, 'nbunch': self._nbunch, 'data':
            self._data, 'default': self._default}

    def __setstate__(self, state):
        self.__init__(**state)

    def __init__(self, viewer, nbunch=None, data=False, default=None):
        self._viewer = viewer
        adjdict = self._adjdict = viewer._adjdict
        if nbunch is None:
            self._nodes_nbrs = adjdict.items
        else:
            nbunch = dict.fromkeys(viewer._graph.nbunch_iter(nbunch))
            self._nodes_nbrs = lambda : [(n, adjdict[n]) for n in nbunch]
        self._nbunch = nbunch
        self._data = data
        self._default = default
        if data is True:
            self._report = lambda n, nbr, dd: (n, nbr, dd)
        elif data is False:
            self._report = lambda n, nbr, dd: (n, nbr)
        else:
            self._report = lambda n, nbr, dd: (n, nbr, dd[data]
                ) if data in dd else (n, nbr, default)

    def __len__(self):
        return sum(len(nbrs) for n, nbrs in self._nodes_nbrs())

    def __iter__(self):
        return (self._report(n, nbr, dd) for n, nbrs in self._nodes_nbrs() for
            nbr, dd in nbrs.items())

    def __contains__(self, e):
        u, v = e[:2]
        if self._nbunch is not None and u not in self._nbunch:
            return False
        try:
            ddict = self._adjdict[u][v]
        except KeyError:
            return False
        return e == self._report(u, v, ddict)

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return f'{self.__class__.__name__}({list(self)})'


class OutEdgeView(Set, Mapping):
    __slots__ = '_adjdict', '_graph', '_nodes_nbrs'

    def __getstate__(self):
        return {'_graph': self._graph}

    def __setstate__(self, state):
        self._graph = G = state['_graph']
        self._adjdict = G._succ if hasattr(G, 'succ') else G._adj
        self._nodes_nbrs = self._adjdict.items

    @classmethod
    def _from_iterable(cls, it):
        return set(it)
    dataview = OutEdgeDataView

    def __init__(self, G):
        self._graph = G
        self._adjdict = G._succ if hasattr(G, 'succ') else G._adj
        self._nodes_nbrs = self._adjdict.items

    def __len__(self):
        return sum(len(nbrs) for n, nbrs in self._nodes_nbrs())

    def __iter__(self):
        for n, nbrs in self._nodes_nbrs():
            for nbr in nbrs:
                yield n, nbr

    def __contains__(self, e):
        try:
            u, v = e
            return v in self._adjdict[u]
        except KeyError:
            return False

    def __getitem__(self, e):
        if isinstance(e, slice):
            raise nx.NetworkXError(
                f'{type(self).__name__} does not support slicing, try list(G.edges)[{e.start}:{e.stop}:{e.step}]'
                )
        u, v = e
        return self._adjdict[u][v]

    def __call__(self, nbunch=None, data=False, default=None):
        if nbunch is None and data is False:
            return self
        return self.dataview(self, nbunch, data, default)

    def data(self, data=True, default=None, nbunch=None):
        if nbunch is None and data is False:
            return self
        return self.dataview(self, nbunch, data, default)

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return f'{self.__class__.__name__}({list(self)})'


class EdgeDataView(OutEdgeDataView):
    __slots__ = ()

    def __len__(self):
        return sum(1 for e in self)

    def __iter__(self):
        seen = {}
        for n, nbrs in self._nodes_nbrs():
            for nbr, dd in nbrs.items():
                if nbr not in seen:
                    yield self._report(n, nbr, dd)
            seen[n] = 1
        del seen

    def __contains__(self, e):
        u, v = e[:2]
        if (self._nbunch is not None and u not in self._nbunch and v not in
            self._nbunch):
            return False
        try:
            ddict = self._adjdict[u][v]
        except KeyError:
            return False
        return e == self._report(u, v, ddict)


class EdgeView(OutEdgeView):
    __slots__ = ()
    dataview = EdgeDataView

    def __len__(self):
        num_nbrs = (len(nbrs) + (n in nbrs) for n, nbrs in self._nodes_nbrs())
        return sum(num_nbrs) // 2

    def __iter__(self):
        seen = {}
        for n, nbrs in self._nodes_nbrs():
            for nbr in list(nbrs):
                if nbr not in seen:
                    yield n, nbr
            seen[n] = 1
        del seen

    def __contains__(self, e):
        try:
            u, v = e[:2]
            return v in self._adjdict[u] or u in self._adjdict[v]
        except (KeyError, ValueError):
            return False


class DiDegreeView:

    def __init__(self, G, nbunch=None, weight=None):
        self._graph = G
        self._succ = G._succ if hasattr(G, '_succ') else G._adj
        self._pred = G._pred if hasattr(G, '_pred') else G._adj
        self._nodes = self._succ if nbunch is None else list(G.nbunch_iter(
            nbunch))
        self._weight = weight

    def __call__(self, nbunch=None, weight=None):
        if nbunch is None:
            if weight == self._weight:
                return self
            return self.__class__(self._graph, None, weight)
        try:
            if nbunch in self._nodes:
                if weight == self._weight:
                    return self[nbunch]
                return self.__class__(self._graph, None, weight)[nbunch]
        except TypeError:
            pass
        return self.__class__(self._graph, nbunch, weight)

    def __getitem__(self, n):
        weight = self._weight
        succs = self._succ[n]
        preds = self._pred[n]
        if weight is None:
            return len(succs) + len(preds)
        return sum(dd.get(weight, 1) for dd in succs.values()) + sum(dd.get
            (weight, 1) for dd in preds.values())

    def __iter__(self):
        weight = self._weight
        if weight is None:
            for n in self._nodes:
                succs = self._succ[n]
                preds = self._pred[n]
                yield n, len(succs) + len(preds)
        else:
            for n in self._nodes:
                succs = self._succ[n]
                preds = self._pred[n]
                deg = sum(dd.get(weight, 1) for dd in succs.values()) + sum(
                    dd.get(weight, 1) for dd in preds.values())
                yield n, deg

    def __len__(self):
        return len(self._nodes)

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return f'{self.__class__.__name__}({dict(self)})'


class DegreeView(DiDegreeView):

    def __getitem__(self, n):
        weight = self._weight
        nbrs = self._succ[n]
        if weight is None:
            return len(nbrs) + (n in nbrs)
        return sum(dd.get(weight, 1) for dd in nbrs.values()) + (n in nbrs and
            nbrs[n].get(weight, 1))

    def __iter__(self):
        weight = self._weight
        if weight is None:
            for n in self._nodes:
                nbrs = self._succ[n]
                yield n, len(nbrs) + (n in nbrs)
        else:
            for n in self._nodes:
                nbrs = self._succ[n]
                deg = sum(dd.get(weight, 1) for dd in nbrs.values()) + (n in
                    nbrs and nbrs[n].get(weight, 1))
                yield n, deg


"""
Base class for undirected graphs.

The Graph class allows any hashable object as a node
and can associate key/value attribute pairs with each undirected edge.

Self-loops are allowed but multiple edges are not (see MultiGraph).

For directed graphs see DiGraph and MultiDiGraph.
"""
from copy import deepcopy
__all__ = ['Graph']


class Graph:
    node_dict_factory = dict
    node_attr_dict_factory = dict
    adjlist_outer_dict_factory = dict
    adjlist_inner_dict_factory = dict
    edge_attr_dict_factory = dict
    graph_attr_dict_factory = dict

    def to_directed_class(self):
        return nx.DiGraph

    def to_undirected_class(self):
        return Graph

    def __init__(self, incoming_graph_data=None, **attr):
        self.graph_attr_dict_factory = self.graph_attr_dict_factory
        self.node_dict_factory = self.node_dict_factory
        self.node_attr_dict_factory = self.node_attr_dict_factory
        self.adjlist_outer_dict_factory = self.adjlist_outer_dict_factory
        self.adjlist_inner_dict_factory = self.adjlist_inner_dict_factory
        self.edge_attr_dict_factory = self.edge_attr_dict_factory
        self.graph = self.graph_attr_dict_factory()
        self._node = self.node_dict_factory()
        self._adj = self.adjlist_outer_dict_factory()
        if incoming_graph_data is not None:
            convert.to_networkx_graph(incoming_graph_data, create_using=self)
        self.graph.update(attr)

    @property
    def adj(self):
        return AdjacencyView(self._adj)

    @property
    def name(self):
        return self.graph.get('name', '')

    @name.setter
    def name(self, s):
        self.graph['name'] = s

    def __str__(self):
        return ''.join([type(self).__name__, f' named {self.name!r}' if
            self.name else '',
            f' with {self.number_of_nodes()} nodes and {self.number_of_edges()} edges'
            ])

    def __iter__(self):
        return iter(self._node)

    def __contains__(self, n):
        try:
            return n in self._node
        except TypeError:
            return False

    def __len__(self):
        return len(self._node)

    def __getitem__(self, n):
        return self.adj[n]

    def add_node(self, node_for_adding, **attr):
        if node_for_adding not in self._node:
            if node_for_adding is None:
                raise ValueError('None cannot be a node')
            self._adj[node_for_adding] = self.adjlist_inner_dict_factory()
            attr_dict = self._node[node_for_adding
                ] = self.node_attr_dict_factory()
            attr_dict.update(attr)
        else:
            self._node[node_for_adding].update(attr)

    def add_nodes_from(self, nodes_for_adding, **attr):
        for n in nodes_for_adding:
            try:
                newnode = n not in self._node
                newdict = attr
            except TypeError:
                n, ndict = n
                newnode = n not in self._node
                newdict = attr.copy()
                newdict.update(ndict)
            if newnode:
                if n is None:
                    raise ValueError('None cannot be a node')
                self._adj[n] = self.adjlist_inner_dict_factory()
                self._node[n] = self.node_attr_dict_factory()
            self._node[n].update(newdict)

    def remove_node(self, n):
        adj = self._adj
        try:
            nbrs = list(adj[n])
            del self._node[n]
        except KeyError as err:
            raise NetworkXError(f'The node {n} is not in the graph.') from err
        for u in nbrs:
            del adj[u][n]
        del adj[n]

    def remove_nodes_from(self, nodes):
        adj = self._adj
        for n in nodes:
            try:
                del self._node[n]
                for u in list(adj[n]):
                    del adj[u][n]
                del adj[n]
            except KeyError:
                pass

    @property
    def nodes(self):
        nodes = NodeView(self)
        self.__dict__['nodes'] = nodes
        return nodes

    def number_of_nodes(self):
        return len(self._node)

    def order(self):
        return len(self._node)

    def has_node(self, n):
        try:
            return n in self._node
        except TypeError:
            return False

    def add_edge(self, u_of_edge, v_of_edge, **attr):
        u, v = u_of_edge, v_of_edge
        if u not in self._node:
            if u is None:
                raise ValueError('None cannot be a node')
            self._adj[u] = self.adjlist_inner_dict_factory()
            self._node[u] = self.node_attr_dict_factory()
        if v not in self._node:
            if v is None:
                raise ValueError('None cannot be a node')
            self._adj[v] = self.adjlist_inner_dict_factory()
            self._node[v] = self.node_attr_dict_factory()
        datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
        datadict.update(attr)
        self._adj[u][v] = datadict
        self._adj[v][u] = datadict

    def add_edges_from(self, ebunch_to_add, **attr):
        for e in ebunch_to_add:
            ne = len(e)
            if ne == 3:
                u, v, dd = e
            elif ne == 2:
                u, v = e
                dd = {}
            else:
                raise NetworkXError(
                    f'Edge tuple {e} must be a 2-tuple or 3-tuple.')
            if u not in self._node:
                if u is None:
                    raise ValueError('None cannot be a node')
                self._adj[u] = self.adjlist_inner_dict_factory()
                self._node[u] = self.node_attr_dict_factory()
            if v not in self._node:
                if v is None:
                    raise ValueError('None cannot be a node')
                self._adj[v] = self.adjlist_inner_dict_factory()
                self._node[v] = self.node_attr_dict_factory()
            datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
            datadict.update(attr)
            datadict.update(dd)
            self._adj[u][v] = datadict
            self._adj[v][u] = datadict

    def add_weighted_edges_from(self, ebunch_to_add, weight='weight', **attr):
        self.add_edges_from(((u, v, {weight: d}) for u, v, d in
            ebunch_to_add), **attr)

    def remove_edge(self, u, v):
        try:
            del self._adj[u][v]
            if u != v:
                del self._adj[v][u]
        except KeyError as err:
            raise NetworkXError(f'The edge {u}-{v} is not in the graph'
                ) from err

    def remove_edges_from(self, ebunch):
        adj = self._adj
        for e in ebunch:
            u, v = e[:2]
            if u in adj and v in adj[u]:
                del adj[u][v]
                if u != v:
                    del adj[v][u]

    def update(self, edges=None, nodes=None):
        if edges is not None:
            if nodes is not None:
                self.add_nodes_from(nodes)
                self.add_edges_from(edges)
            else:
                try:
                    graph_nodes = edges.nodes
                    graph_edges = edges.edges
                except AttributeError:
                    self.add_edges_from(edges)
                else:
                    self.add_nodes_from(graph_nodes.data())
                    self.add_edges_from(graph_edges.data())
                    self.graph.update(edges.graph)
        elif nodes is not None:
            self.add_nodes_from(nodes)
        else:
            raise NetworkXError('update needs nodes or edges input')

    def has_edge(self, u, v):
        try:
            return v in self._adj[u]
        except KeyError:
            return False

    def neighbors(self, n):
        try:
            return iter(self._adj[n])
        except KeyError as err:
            raise NetworkXError(f'The node {n} is not in the graph.') from err

    @property
    def edges(self):
        return EdgeView(self)

    def get_edge_data(self, u, v, default=None):
        try:
            return self._adj[u][v]
        except KeyError:
            return default

    def adjacency(self):
        return iter(self._adj.items())

    @property
    def degree(self):
        return DegreeView(self)

    def clear(self):
        self._adj.clear()
        self._node.clear()
        self.graph.clear()

    def clear_edges(self):
        for neighbours_dict in self._adj.values():
            neighbours_dict.clear()

    def is_multigraph(self):
        return False

    def is_directed(self):
        return False

    def copy(self, as_view=False):
        if as_view is True:
            return nx.graphviews.generic_graph_view(self)
        G = self.__class__()
        G.graph.update(self.graph)
        G.add_nodes_from((n, d.copy()) for n, d in self._node.items())
        G.add_edges_from((u, v, datadict.copy()) for u, nbrs in self._adj.
            items() for v, datadict in nbrs.items())
        return G

    def to_directed(self, as_view=False):
        graph_class = self.to_directed_class()
        if as_view is True:
            return nx.graphviews.generic_graph_view(self, graph_class)
        G = graph_class()
        G.graph.update(deepcopy(self.graph))
        G.add_nodes_from((n, deepcopy(d)) for n, d in self._node.items())
        G.add_edges_from((u, v, deepcopy(data)) for u, nbrs in self._adj.
            items() for v, data in nbrs.items())
        return G

    def to_undirected(self, as_view=False):
        graph_class = self.to_undirected_class()
        if as_view is True:
            return nx.graphviews.generic_graph_view(self, graph_class)
        G = graph_class()
        G.graph.update(deepcopy(self.graph))
        G.add_nodes_from((n, deepcopy(d)) for n, d in self._node.items())
        G.add_edges_from((u, v, deepcopy(d)) for u, nbrs in self._adj.items
            () for v, d in nbrs.items())
        return G

    def subgraph(self, nodes):
        induced_nodes = nx.filters.show_nodes(self.nbunch_iter(nodes))
        subgraph = nx.graphviews.subgraph_view
        if hasattr(self, '_NODE_OK'):
            return subgraph(self._graph, induced_nodes, self._EDGE_OK)
        return subgraph(self, induced_nodes)

    def edge_subgraph(self, edges):
        return nx.edge_subgraph(self, edges)

    def size(self, weight=None):
        s = sum(d for v, d in self.degree(weight=weight))
        return s // 2 if weight is None else s / 2

    def number_of_edges(self, u=None, v=None):
        if u is None:
            return int(self.size())
        if v in self._adj[u]:
            return 1
        return 0

    def nbunch_iter(self, nbunch=None):
        if nbunch is None:
            bunch = iter(self._adj)
        elif nbunch in self:
            bunch = iter([nbunch])
        else:

            def bunch_iter(nlist, adj):
                try:
                    for n in nlist:
                        if n in adj:
                            yield n
                except TypeError as err:
                    exc, message = err, err.args[0]
                    if 'iter' in message:
                        exc = NetworkXError(
                            'nbunch is not a node or a sequence of nodes.')
                    if 'hashable' in message:
                        exc = NetworkXError(
                            f'Node {n} in sequence nbunch is not a valid node.'
                            )
                    raise exc
            bunch = bunch_iter(nbunch, self._adj)
        return bunch


"""Base class for directed graphs."""
from copy import deepcopy
__all__ = ['DiGraph']


class DiGraph(Graph):

    def __init__(self, incoming_graph_data=None, **attr):
        self.graph_attr_dict_factory = self.graph_attr_dict_factory
        self.node_dict_factory = self.node_dict_factory
        self.node_attr_dict_factory = self.node_attr_dict_factory
        self.adjlist_outer_dict_factory = self.adjlist_outer_dict_factory
        self.adjlist_inner_dict_factory = self.adjlist_inner_dict_factory
        self.edge_attr_dict_factory = self.edge_attr_dict_factory
        self.graph = self.graph_attr_dict_factory()
        self._node = self.node_dict_factory()
        self._adj = self.adjlist_outer_dict_factory()
        self._pred = self.adjlist_outer_dict_factory()
        self._succ = self._adj
        if incoming_graph_data is not None:
            convert.to_networkx_graph(incoming_graph_data, create_using=self)
        self.graph.update(attr)

    @property
    def adj(self):
        return AdjacencyView(self._succ)

    @property
    def succ(self):
        return AdjacencyView(self._succ)

    @property
    def pred(self):
        return AdjacencyView(self._pred)

    def add_node(self, node_for_adding, **attr):
        if node_for_adding not in self._succ:
            if node_for_adding is None:
                raise ValueError('None cannot be a node')
            self._succ[node_for_adding] = self.adjlist_inner_dict_factory()
            self._pred[node_for_adding] = self.adjlist_inner_dict_factory()
            attr_dict = self._node[node_for_adding
                ] = self.node_attr_dict_factory()
            attr_dict.update(attr)
        else:
            self._node[node_for_adding].update(attr)

    def add_nodes_from(self, nodes_for_adding, **attr):
        for n in nodes_for_adding:
            try:
                newnode = n not in self._node
                newdict = attr
            except TypeError:
                n, ndict = n
                newnode = n not in self._node
                newdict = attr.copy()
                newdict.update(ndict)
            if newnode:
                if n is None:
                    raise ValueError('None cannot be a node')
                self._succ[n] = self.adjlist_inner_dict_factory()
                self._pred[n] = self.adjlist_inner_dict_factory()
                self._node[n] = self.node_attr_dict_factory()
            self._node[n].update(newdict)

    def remove_node(self, n):
        try:
            nbrs = self._succ[n]
            del self._node[n]
        except KeyError as err:
            raise NetworkXError(f'The node {n} is not in the digraph.'
                ) from err
        for u in nbrs:
            del self._pred[u][n]
        del self._succ[n]
        for u in self._pred[n]:
            del self._succ[u][n]
        del self._pred[n]

    def remove_nodes_from(self, nodes):
        for n in nodes:
            try:
                succs = self._succ[n]
                del self._node[n]
                for u in succs:
                    del self._pred[u][n]
                del self._succ[n]
                for u in self._pred[n]:
                    del self._succ[u][n]
                del self._pred[n]
            except KeyError:
                pass

    def add_edge(self, u_of_edge, v_of_edge, **attr):
        u, v = u_of_edge, v_of_edge
        if u not in self._succ:
            if u is None:
                raise ValueError('None cannot be a node')
            self._succ[u] = self.adjlist_inner_dict_factory()
            self._pred[u] = self.adjlist_inner_dict_factory()
            self._node[u] = self.node_attr_dict_factory()
        if v not in self._succ:
            if v is None:
                raise ValueError('None cannot be a node')
            self._succ[v] = self.adjlist_inner_dict_factory()
            self._pred[v] = self.adjlist_inner_dict_factory()
            self._node[v] = self.node_attr_dict_factory()
        datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
        datadict.update(attr)
        self._succ[u][v] = datadict
        self._pred[v][u] = datadict

    def add_edges_from(self, ebunch_to_add, **attr):
        for e in ebunch_to_add:
            ne = len(e)
            if ne == 3:
                u, v, dd = e
            elif ne == 2:
                u, v = e
                dd = {}
            else:
                raise NetworkXError(
                    f'Edge tuple {e} must be a 2-tuple or 3-tuple.')
            if u not in self._succ:
                if u is None:
                    raise ValueError('None cannot be a node')
                self._succ[u] = self.adjlist_inner_dict_factory()
                self._pred[u] = self.adjlist_inner_dict_factory()
                self._node[u] = self.node_attr_dict_factory()
            if v not in self._succ:
                if v is None:
                    raise ValueError('None cannot be a node')
                self._succ[v] = self.adjlist_inner_dict_factory()
                self._pred[v] = self.adjlist_inner_dict_factory()
                self._node[v] = self.node_attr_dict_factory()
            datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
            datadict.update(attr)
            datadict.update(dd)
            self._succ[u][v] = datadict
            self._pred[v][u] = datadict

    def remove_edge(self, u, v):
        try:
            del self._succ[u][v]
            del self._pred[v][u]
        except KeyError as err:
            raise NetworkXError(f'The edge {u}-{v} not in graph.') from err

    def remove_edges_from(self, ebunch):
        for e in ebunch:
            u, v = e[:2]
            if u in self._succ and v in self._succ[u]:
                del self._succ[u][v]
                del self._pred[v][u]

    def has_successor(self, u, v):
        return u in self._succ and v in self._succ[u]

    def has_predecessor(self, u, v):
        return u in self._pred and v in self._pred[u]

    def successors(self, n):
        try:
            return iter(self._succ[n])
        except KeyError as err:
            raise NetworkXError(f'The node {n} is not in the digraph.'
                ) from err
    neighbors = successors

    def predecessors(self, n):
        try:
            return iter(self._pred[n])
        except KeyError as err:
            raise NetworkXError(f'The node {n} is not in the digraph.'
                ) from err

    @property
    def edges(self):
        return OutEdgeView(self)
    out_edges = edges

    @property
    def in_edges(self):
        return InEdgeView(self)

    @property
    def degree(self):
        return DiDegreeView(self)

    @property
    def in_degree(self):
        return InDegreeView(self)

    @property
    def out_degree(self):
        return OutDegreeView(self)

    def clear(self):
        self._succ.clear()
        self._pred.clear()
        self._node.clear()
        self.graph.clear()

    def clear_edges(self):
        for predecessor_dict in self._pred.values():
            predecessor_dict.clear()
        for successor_dict in self._succ.values():
            successor_dict.clear()

    def is_multigraph(self):
        return False

    def is_directed(self):
        return True

    def to_undirected(self, reciprocal=False, as_view=False):
        graph_class = self.to_undirected_class()
        if as_view is True:
            return nx.graphviews.generic_graph_view(self, graph_class)
        G = graph_class()
        G.graph.update(deepcopy(self.graph))
        G.add_nodes_from((n, deepcopy(d)) for n, d in self._node.items())
        if reciprocal is True:
            G.add_edges_from((u, v, deepcopy(d)) for u, nbrs in self._adj.
                items() for v, d in nbrs.items() if v in self._pred[u])
        else:
            G.add_edges_from((u, v, deepcopy(d)) for u, nbrs in self._adj.
                items() for v, d in nbrs.items())
        return G

    def reverse(self, copy=True):
        if copy:
            H = self.__class__()
            H.graph.update(deepcopy(self.graph))
            H.add_nodes_from((n, deepcopy(d)) for n, d in self.nodes.items())
            H.add_edges_from((v, u, deepcopy(d)) for u, v, d in self.edges(
                data=True))
            return H
        return nx.graphviews.reverse_view(self)


class networkx:
    Graph = Graph
    DiGraph = DiGraph
    NetworkXException = Exception


nx = networkx
"""Functions to convert NetworkX graphs to and from other formats.

The preferred way of converting data to a NetworkX graph is through the
graph constructor.  The constructor calls the to_networkx_graph() function
which attempts to guess the input type and convert it automatically.

Examples
--------
Create a graph with a single edge from a dictionary of dictionaries

>>> d = {0: {1: 1}}  # dict-of-dicts single edge (0,1)
>>> G = nx.Graph(d)

See Also
--------
nx_agraph, nx_pydot
"""
import warnings
from collections.abc import Collection, Generator, Iterator
__all__ = ['to_networkx_graph', 'from_dict_of_dicts', 'to_dict_of_dicts',
    'from_dict_of_lists', 'to_dict_of_lists', 'from_edgelist', 'to_edgelist']


def to_networkx_graph(data, create_using=None, multigraph_input=False):
    if hasattr(data, 'adj'):
        try:
            return deepcopy(data)
        except Exception as e:
            print(e)
            raise nx.NetworkXError('Input is not a correct NetworkX graph.'
                ) from e
    if hasattr(data, 'is_strict'):
        try:
            return nx.nx_agraph.from_agraph(data, create_using=create_using)
        except Exception as e:
            raise nx.NetworkXError('Input is not a correct pygraphviz graph.'
                ) from e
    if isinstance(data, dict):
        try:
            return from_dict_of_dicts(data, create_using=create_using,
                multigraph_input=multigraph_input)
        except:
            try:
                return from_dict_of_lists(data, create_using=create_using)
            except Exception as e:
                raise TypeError('Input is not known type.') from e
    try:
        import pandas as pd
        if isinstance(data, pd.DataFrame):
            if data.shape[0] == data.shape[1]:
                try:
                    return nx.from_pandas_adjacency(data, create_using=
                        create_using)
                except Exception as e:
                    msg = (
                        'Input is not a correct Pandas DataFrame adjacency matrix.'
                        )
                    raise nx.NetworkXError(msg) from e
            else:
                try:
                    return nx.from_pandas_edgelist(data, edge_attr=True,
                        create_using=create_using)
                except Exception as e:
                    msg = 'Input is not a correct Pandas DataFrame edge-list.'
                    raise nx.NetworkXError(msg) from e
    except ImportError:
        warnings.warn('pandas not found, skipping conversion test.',
            ImportWarning)
    try:
        import numpy as np
        if isinstance(data, (np.matrix, np.ndarray)):
            try:
                return nx.from_numpy_matrix(data, create_using=create_using)
            except Exception as e:
                raise nx.NetworkXError(
                    'Input is not a correct numpy matrix or array.') from e
    except ImportError:
        warnings.warn('numpy not found, skipping conversion test.',
            ImportWarning)
    try:
        import scipy
        if hasattr(data, 'format'):
            try:
                return nx.from_scipy_sparse_matrix(data, create_using=
                    create_using)
            except Exception as e:
                raise nx.NetworkXError(
                    'Input is not a correct scipy sparse matrix type.') from e
    except ImportError:
        warnings.warn('scipy not found, skipping conversion test.',
            ImportWarning)
    if isinstance(data, (Collection, Generator, Iterator)):
        try:
            return from_edgelist(data, create_using=create_using)
        except Exception as e:
            raise nx.NetworkXError('Input is not a valid edge list') from e
    raise nx.NetworkXError('Input is not a known data type for conversion.')


class convert:
    to_networkx_graph = to_networkx_graph


from collections import defaultdict
__all__ = ['check_planarity', 'PlanarEmbedding']


def check_planarity(G, counterexample=False):
    planarity_state = LRPlanarity(G)
    embedding = planarity_state.lr_planarity()
    if embedding is None:
        if counterexample:
            return False, get_counterexample(G)
        else:
            return False, None
    else:
        return True, embedding


def check_planarity_recursive(G, counterexample=False):
    planarity_state = LRPlanarity(G)
    embedding = planarity_state.lr_planarity_recursive()
    if embedding is None:
        if counterexample:
            return False, get_counterexample_recursive(G)
        else:
            return False, None
    else:
        return True, embedding


def get_counterexample(G):
    G = nx.Graph(G)
    if check_planarity(G)[0]:
        raise nx.NetworkXException('G is planar - no counter example.')
    subgraph = nx.Graph()
    for u in G:
        nbrs = list(G[u])
        for v in nbrs:
            G.remove_edge(u, v)
            if check_planarity(G)[0]:
                G.add_edge(u, v)
                subgraph.add_edge(u, v)
    return subgraph


def get_counterexample_recursive(G):
    G = nx.Graph(G)
    if check_planarity_recursive(G)[0]:
        raise nx.NetworkXException('G is planar - no counter example.')
    subgraph = nx.Graph()
    for u in G:
        nbrs = list(G[u])
        for v in nbrs:
            G.remove_edge(u, v)
            if check_planarity_recursive(G)[0]:
                G.add_edge(u, v)
                subgraph.add_edge(u, v)
    return subgraph


class Interval:

    def __init__(self, low=None, high=None):
        self.low = low
        self.high = high

    def empty(self):
        return self.low is None and self.high is None

    def copy(self):
        return Interval(self.low, self.high)

    def conflicting(self, b, planarity_state):
        return not self.empty() and planarity_state.lowpt[self.high
            ] > planarity_state.lowpt[b]


class ConflictPair:

    def __init__(self, left=Interval(), right=Interval()):
        self.left = left
        self.right = right

    def swap(self):
        temp = self.left
        self.left = self.right
        self.right = temp

    def lowest(self, planarity_state):
        if self.left.empty():
            return planarity_state.lowpt[self.right.low]
        if self.right.empty():
            return planarity_state.lowpt[self.left.low]
        return min(planarity_state.lowpt[self.left.low], planarity_state.
            lowpt[self.right.low])


def top_of_stack(l):
    if not l:
        return None
    return l[-1]


class LRPlanarity:
    __slots__ = ['G', 'roots', 'height', 'lowpt', 'lowpt2', 'nesting_depth',
        'parent_edge', 'DG', 'adjs', 'ordered_adjs', 'ref', 'side', 'S',
        'stack_bottom', 'lowpt_edge', 'left_ref', 'right_ref', 'embedding']

    def __init__(self, G):
        self.G = nx.Graph()
        self.G.add_nodes_from(G.nodes)
        for e in G.edges:
            if e[0] != e[1]:
                self.G.add_edge(e[0], e[1])
        self.roots = []
        self.height = defaultdict(lambda : None)
        self.lowpt = {}
        self.lowpt2 = {}
        self.nesting_depth = {}
        self.parent_edge = defaultdict(lambda : None)
        self.DG = nx.DiGraph()
        self.DG.add_nodes_from(G.nodes)
        self.adjs = {}
        self.ordered_adjs = {}
        self.ref = defaultdict(lambda : None)
        self.side = defaultdict(lambda : 1)
        self.S = []
        self.stack_bottom = {}
        self.lowpt_edge = {}
        self.left_ref = {}
        self.right_ref = {}
        self.embedding = PlanarEmbedding()

    def lr_planarity(self):
        if self.G.order() > 2 and self.G.size() > 3 * self.G.order() - 6:
            return None
        for v in self.G:
            self.adjs[v] = list(self.G[v])
        for v in self.G:
            if self.height[v] is None:
                self.height[v] = 0
                self.roots.append(v)
                self.dfs_orientation(v)
        self.G = None
        self.lowpt2 = None
        self.adjs = None
        for v in self.DG:
            self.ordered_adjs[v] = sorted(self.DG[v], key=lambda x: self.
                nesting_depth[v, x])
        for v in self.roots:
            if not self.dfs_testing(v):
                return None
        self.height = None
        self.lowpt = None
        self.S = None
        self.stack_bottom = None
        self.lowpt_edge = None
        for e in self.DG.edges:
            self.nesting_depth[e] = self.sign(e) * self.nesting_depth[e]
        self.embedding.add_nodes_from(self.DG.nodes)
        for v in self.DG:
            self.ordered_adjs[v] = sorted(self.DG[v], key=lambda x: self.
                nesting_depth[v, x])
            previous_node = None
            for w in self.ordered_adjs[v]:
                self.embedding.add_half_edge_cw(v, w, previous_node)
                previous_node = w
        self.DG = None
        self.nesting_depth = None
        self.ref = None
        for v in self.roots:
            self.dfs_embedding(v)
        self.roots = None
        self.parent_edge = None
        self.ordered_adjs = None
        self.left_ref = None
        self.right_ref = None
        self.side = None
        return self.embedding

    def lr_planarity_recursive(self):
        if self.G.order() > 2 and self.G.size() > 3 * self.G.order() - 6:
            return None
        for v in self.G:
            if self.height[v] is None:
                self.height[v] = 0
                self.roots.append(v)
                self.dfs_orientation_recursive(v)
        self.G = None
        for v in self.DG:
            self.ordered_adjs[v] = sorted(self.DG[v], key=lambda x: self.
                nesting_depth[v, x])
        for v in self.roots:
            if not self.dfs_testing_recursive(v):
                return None
        for e in self.DG.edges:
            self.nesting_depth[e] = self.sign_recursive(e
                ) * self.nesting_depth[e]
        self.embedding.add_nodes_from(self.DG.nodes)
        for v in self.DG:
            self.ordered_adjs[v] = sorted(self.DG[v], key=lambda x: self.
                nesting_depth[v, x])
            previous_node = None
            for w in self.ordered_adjs[v]:
                self.embedding.add_half_edge_cw(v, w, previous_node)
                previous_node = w
        for v in self.roots:
            self.dfs_embedding_recursive(v)
        return self.embedding

    def dfs_orientation(self, v):
        dfs_stack = [v]
        ind = defaultdict(lambda : 0)
        skip_init = defaultdict(lambda : False)
        while dfs_stack:
            v = dfs_stack.pop()
            e = self.parent_edge[v]
            for w in self.adjs[v][ind[v]:]:
                vw = v, w
                if not skip_init[vw]:
                    if (v, w) in self.DG.edges or (w, v) in self.DG.edges:
                        ind[v] += 1
                        continue
                    self.DG.add_edge(v, w)
                    self.lowpt[vw] = self.height[v]
                    self.lowpt2[vw] = self.height[v]
                    if self.height[w] is None:
                        self.parent_edge[w] = vw
                        self.height[w] = self.height[v] + 1
                        dfs_stack.append(v)
                        dfs_stack.append(w)
                        skip_init[vw] = True
                        break
                    else:
                        self.lowpt[vw] = self.height[w]
                self.nesting_depth[vw] = 2 * self.lowpt[vw]
                if self.lowpt2[vw] < self.height[v]:
                    self.nesting_depth[vw] += 1
                if e is not None:
                    if self.lowpt[vw] < self.lowpt[e]:
                        self.lowpt2[e] = min(self.lowpt[e], self.lowpt2[vw])
                        self.lowpt[e] = self.lowpt[vw]
                    elif self.lowpt[vw] > self.lowpt[e]:
                        self.lowpt2[e] = min(self.lowpt2[e], self.lowpt[vw])
                    else:
                        self.lowpt2[e] = min(self.lowpt2[e], self.lowpt2[vw])
                ind[v] += 1

    def dfs_orientation_recursive(self, v):
        e = self.parent_edge[v]
        for w in self.G[v]:
            if (v, w) in self.DG.edges or (w, v) in self.DG.edges:
                continue
            vw = v, w
            self.DG.add_edge(v, w)
            self.lowpt[vw] = self.height[v]
            self.lowpt2[vw] = self.height[v]
            if self.height[w] is None:
                self.parent_edge[w] = vw
                self.height[w] = self.height[v] + 1
                self.dfs_orientation_recursive(w)
            else:
                self.lowpt[vw] = self.height[w]
            self.nesting_depth[vw] = 2 * self.lowpt[vw]
            if self.lowpt2[vw] < self.height[v]:
                self.nesting_depth[vw] += 1
            if e is not None:
                if self.lowpt[vw] < self.lowpt[e]:
                    self.lowpt2[e] = min(self.lowpt[e], self.lowpt2[vw])
                    self.lowpt[e] = self.lowpt[vw]
                elif self.lowpt[vw] > self.lowpt[e]:
                    self.lowpt2[e] = min(self.lowpt2[e], self.lowpt[vw])
                else:
                    self.lowpt2[e] = min(self.lowpt2[e], self.lowpt2[vw])

    def dfs_testing(self, v):
        dfs_stack = [v]
        ind = defaultdict(lambda : 0)
        skip_init = defaultdict(lambda : False)
        while dfs_stack:
            v = dfs_stack.pop()
            e = self.parent_edge[v]
            skip_final = False
            for w in self.ordered_adjs[v][ind[v]:]:
                ei = v, w
                if not skip_init[ei]:
                    self.stack_bottom[ei] = top_of_stack(self.S)
                    if ei == self.parent_edge[w]:
                        dfs_stack.append(v)
                        dfs_stack.append(w)
                        skip_init[ei] = True
                        skip_final = True
                        break
                    else:
                        self.lowpt_edge[ei] = ei
                        self.S.append(ConflictPair(right=Interval(ei, ei)))
                if self.lowpt[ei] < self.height[v]:
                    if w == self.ordered_adjs[v][0]:
                        self.lowpt_edge[e] = self.lowpt_edge[ei]
                    elif not self.add_constraints(ei, e):
                        return False
                ind[v] += 1
            if not skip_final:
                if e is not None:
                    self.remove_back_edges(e)
        return True

    def dfs_testing_recursive(self, v):
        e = self.parent_edge[v]
        for w in self.ordered_adjs[v]:
            ei = v, w
            self.stack_bottom[ei] = top_of_stack(self.S)
            if ei == self.parent_edge[w]:
                if not self.dfs_testing_recursive(w):
                    return False
            else:
                self.lowpt_edge[ei] = ei
                self.S.append(ConflictPair(right=Interval(ei, ei)))
            if self.lowpt[ei] < self.height[v]:
                if w == self.ordered_adjs[v][0]:
                    self.lowpt_edge[e] = self.lowpt_edge[ei]
                elif not self.add_constraints(ei, e):
                    return False
        if e is not None:
            self.remove_back_edges(e)
        return True

    def add_constraints(self, ei, e):
        P = ConflictPair()
        while True:
            Q = self.S.pop()
            if not Q.left.empty():
                Q.swap()
            if not Q.left.empty():
                return False
            if self.lowpt[Q.right.low] > self.lowpt[e]:
                if P.right.empty():
                    P.right = Q.right.copy()
                else:
                    self.ref[P.right.low] = Q.right.high
                P.right.low = Q.right.low
            else:
                self.ref[Q.right.low] = self.lowpt_edge[e]
            if top_of_stack(self.S) == self.stack_bottom[ei]:
                break
        while top_of_stack(self.S).left.conflicting(ei, self) or top_of_stack(
            self.S).right.conflicting(ei, self):
            Q = self.S.pop()
            if Q.right.conflicting(ei, self):
                Q.swap()
            if Q.right.conflicting(ei, self):
                return False
            self.ref[P.right.low] = Q.right.high
            if Q.right.low is not None:
                P.right.low = Q.right.low
            if P.left.empty():
                P.left = Q.left.copy()
            else:
                self.ref[P.left.low] = Q.left.high
            P.left.low = Q.left.low
        if not (P.left.empty() and P.right.empty()):
            self.S.append(P)
        return True

    def remove_back_edges(self, e):
        u = e[0]
        while self.S and top_of_stack(self.S).lowest(self) == self.height[u]:
            P = self.S.pop()
            if P.left.low is not None:
                self.side[P.left.low] = -1
        if self.S:
            P = self.S.pop()
            while P.left.high is not None and P.left.high[1] == u:
                P.left.high = self.ref[P.left.high]
            if P.left.high is None and P.left.low is not None:
                self.ref[P.left.low] = P.right.low
                self.side[P.left.low] = -1
                P.left.low = None
            while P.right.high is not None and P.right.high[1] == u:
                P.right.high = self.ref[P.right.high]
            if P.right.high is None and P.right.low is not None:
                self.ref[P.right.low] = P.left.low
                self.side[P.right.low] = -1
                P.right.low = None
            self.S.append(P)
        if self.lowpt[e] < self.height[u]:
            hl = top_of_stack(self.S).left.high
            hr = top_of_stack(self.S).right.high
            if hl is not None and (hr is None or self.lowpt[hl] > self.
                lowpt[hr]):
                self.ref[e] = hl
            else:
                self.ref[e] = hr

    def dfs_embedding(self, v):
        dfs_stack = [v]
        ind = defaultdict(lambda : 0)
        while dfs_stack:
            v = dfs_stack.pop()
            for w in self.ordered_adjs[v][ind[v]:]:
                ind[v] += 1
                ei = v, w
                if ei == self.parent_edge[w]:
                    self.embedding.add_half_edge_first(w, v)
                    self.left_ref[v] = w
                    self.right_ref[v] = w
                    dfs_stack.append(v)
                    dfs_stack.append(w)
                    break
                elif self.side[ei] == 1:
                    self.embedding.add_half_edge_cw(w, v, self.right_ref[w])
                else:
                    self.embedding.add_half_edge_ccw(w, v, self.left_ref[w])
                    self.left_ref[w] = v

    def dfs_embedding_recursive(self, v):
        for w in self.ordered_adjs[v]:
            ei = v, w
            if ei == self.parent_edge[w]:
                self.embedding.add_half_edge_first(w, v)
                self.left_ref[v] = w
                self.right_ref[v] = w
                self.dfs_embedding_recursive(w)
            elif self.side[ei] == 1:
                self.embedding.add_half_edge_cw(w, v, self.right_ref[w])
            else:
                self.embedding.add_half_edge_ccw(w, v, self.left_ref[w])
                self.left_ref[w] = v

    def sign(self, e):
        dfs_stack = [e]
        old_ref = defaultdict(lambda : None)
        while dfs_stack:
            e = dfs_stack.pop()
            if self.ref[e] is not None:
                dfs_stack.append(e)
                dfs_stack.append(self.ref[e])
                old_ref[e] = self.ref[e]
                self.ref[e] = None
            else:
                self.side[e] *= self.side[old_ref[e]]
        return self.side[e]

    def sign_recursive(self, e):
        if self.ref[e] is not None:
            self.side[e] = self.side[e] * self.sign_recursive(self.ref[e])
            self.ref[e] = None
        return self.side[e]


class PlanarEmbedding(nx.DiGraph):

    def get_data(self):
        embedding = dict()
        for v in self:
            embedding[v] = list(self.neighbors_cw_order(v))
        return embedding

    def set_data(self, data):
        for v in data:
            for w in reversed(data[v]):
                self.add_half_edge_first(v, w)

    def neighbors_cw_order(self, v):
        if len(self[v]) == 0:
            return
        start_node = self.nodes[v]['first_nbr']
        yield start_node
        current_node = self[v][start_node]['cw']
        while start_node != current_node:
            yield current_node
            current_node = self[v][current_node]['cw']

    def check_structure(self):
        for v in self:
            try:
                sorted_nbrs = set(self.neighbors_cw_order(v))
            except KeyError as err:
                msg = (
                    f'Bad embedding. Missing orientation for a neighbor of {v}'
                    )
                raise nx.NetworkXException(msg) from err
            unsorted_nbrs = set(self[v])
            if sorted_nbrs != unsorted_nbrs:
                msg = 'Bad embedding. Edge orientations not set correctly.'
                raise nx.NetworkXException(msg)
            for w in self[v]:
                if not self.has_edge(w, v):
                    msg = 'Bad embedding. Opposite half-edge is missing.'
                    raise nx.NetworkXException(msg)
        counted_half_edges = set()
        for component in nx.connected_components(self):
            if len(component) == 1:
                continue
            num_nodes = len(component)
            num_half_edges = 0
            num_faces = 0
            for v in component:
                for w in self.neighbors_cw_order(v):
                    num_half_edges += 1
                    if (v, w) not in counted_half_edges:
                        num_faces += 1
                        self.traverse_face(v, w, counted_half_edges)
            num_edges = num_half_edges // 2
            if num_nodes - num_edges + num_faces != 2:
                msg = "Bad embedding. The graph does not match Euler's formula"
                raise nx.NetworkXException(msg)

    def add_half_edge_ccw(self, start_node, end_node, reference_neighbor):
        if reference_neighbor is None:
            self.add_edge(start_node, end_node)
            self[start_node][end_node]['cw'] = end_node
            self[start_node][end_node]['ccw'] = end_node
            self.nodes[start_node]['first_nbr'] = end_node
        else:
            ccw_reference = self[start_node][reference_neighbor]['ccw']
            self.add_half_edge_cw(start_node, end_node, ccw_reference)
            if reference_neighbor == self.nodes[start_node].get('first_nbr',
                None):
                self.nodes[start_node]['first_nbr'] = end_node

    def add_half_edge_cw(self, start_node, end_node, reference_neighbor):
        self.add_edge(start_node, end_node)
        if reference_neighbor is None:
            self[start_node][end_node]['cw'] = end_node
            self[start_node][end_node]['ccw'] = end_node
            self.nodes[start_node]['first_nbr'] = end_node
            return
        if reference_neighbor not in self[start_node]:
            raise nx.NetworkXException(
                'Cannot add edge. Reference neighbor does not exist')
        cw_reference = self[start_node][reference_neighbor]['cw']
        self[start_node][reference_neighbor]['cw'] = end_node
        self[start_node][end_node]['cw'] = cw_reference
        self[start_node][cw_reference]['ccw'] = end_node
        self[start_node][end_node]['ccw'] = reference_neighbor

    def connect_components(self, v, w):
        self.add_half_edge_first(v, w)
        self.add_half_edge_first(w, v)

    def add_half_edge_first(self, start_node, end_node):
        if start_node in self and 'first_nbr' in self.nodes[start_node]:
            reference = self.nodes[start_node]['first_nbr']
        else:
            reference = None
        self.add_half_edge_ccw(start_node, end_node, reference)

    def next_face_half_edge(self, v, w):
        new_node = self[w][v]['ccw']
        return w, new_node

    def traverse_face(self, v, w, mark_half_edges=None):
        if mark_half_edges is None:
            mark_half_edges = set()
        face_nodes = [v]
        mark_half_edges.add((v, w))
        prev_node = v
        cur_node = w
        incoming_node = self[v][w]['cw']
        while cur_node != v or prev_node != incoming_node:
            face_nodes.append(cur_node)
            prev_node, cur_node = self.next_face_half_edge(prev_node, cur_node)
            if (prev_node, cur_node) in mark_half_edges:
                raise nx.NetworkXException(
                    'Bad planar embedding. Impossible face.')
            mark_half_edges.add((prev_node, cur_node))
        return face_nodes

    def is_directed(self):
        return False

