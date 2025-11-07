#!/bin/bash
echo "Started cleanup"
docker stop ft_onion_container
docker rm ft_onion_container
docker rmi ft_onion

echo "Verifying cleanup..."
if docker ps -a | grep -q ft_onion; then
    echo "❌ FAILED: ft_onion containers still exist"
else
    echo "✅ SUCCESS: No ft_onion containers found"
fi

if docker images | grep -q ft_onion; then
    echo "❌ FAILED: ft_onion images still exist"
else
    echo "✅ SUCCESS: No ft_onion images found"
fi

echo "Cleanup complete!"