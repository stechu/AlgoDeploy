How to run a private Algorand network
=====================================

1. Install Algorand, to make sure you installed correctly, check:
```
goal --version
```
It will show something like this:
```
8590000131
2.1.3.dev [HEAD] (commit #17fa1f1c)
go-algorand is licensed with AGPLv3.0
```

2. Find a local deployment template, here we use `go-algorand/test/testdata/nettemplates/TwoNodes50EachFuture.json`, then run
```
goal network create -n <your_network_name> -t <template_file> -r <your_blockchain_folder>
```
This will create a root folder for your blockchain, under the root folder, it will also create two data folder for each node, one is `Primary', the other is `Node`.

3. Now, we start the network:
```
goal network start -n <your_network_name> -r <your_blockchain_folder>
```
This will start the network.
To test whether your start the network sucessfully, you can run `carpenter`:
```
carpenter -d <your_blockchain_folder>/Node/
``
`
