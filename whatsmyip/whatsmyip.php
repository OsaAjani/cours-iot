<?php
    $user = '';
    $password = '';
    $database = 'whatsmyip';

    //Try connect to bdd
    try {
        $pdo = new PDO('mysql:host=localhost;dbname=' . $database, $user, $password);
    } catch (PDOException $e) {
        print "Erreur !: " . $e->getMessage() . "<br/>";
        die();
    }

    //Get ips
    $ips_query = 'SELECT * FROM ips';
    $query = $pdo->prepare($ips_query);
    $query->execute();
    $ips = $query->fetchAll();


    //Insert ips
    $public_ip = $_SERVER['REMOTE_ADDR'];
    $local_ip = $_GET['local_ip'] ?? false;
    $hostname = $_GET['hostname'] ?? false;
    $at = new \DateTime();

    if ($public_ip && $local_ip && $hostname)
    {
        $insert_query = 'INSERT INTO ips (public_ip, local_ip, hostname, at) VALUES (:public_ip, :local_ip, :hostname, :at)';
        $query = $pdo->prepare($insert_query);
        $query->execute([
            'public_ip' => $public_ip,
            'local_ip' => $local_ip,
            'hostname' => $hostname,
            'at' => $at->format('Y-m-d H:i:s'),
        ]);
    }
?>
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Whatsmyip</title>
    <style>
        td,
        th {
            border: 1px solid black;
            padding: 5px 10px;    
        }

        table {
            border-collapse: collapse;
            width: 50%;
        }
    </style>  
</head>
<body>
    <h1>Liste des IP et hostname associés</h1>
    <table>
        <tr>
            <th>Date</th>
            <th>Ip Publique</th>
            <th>Ip Interne</th>
            <th>Hostname</th>
        </tr>
        <?php foreach ($ips as $ip) { ?>
            <tr>
                <td><?php echo htmlspecialchars($ip['at']); ?></td>
                <td><?php echo htmlspecialchars($ip['public_ip']); ?></td>
                <td><?php echo htmlspecialchars($ip['local_ip']); ?></td>
                <td><?php echo htmlspecialchars($ip['hostname']); ?></td>
            </tr>
        <?php } ?>
    </table>
</body>
</html>
