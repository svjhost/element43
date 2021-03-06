from apps.market_data.models import Orders, OrderHistory, ItemRegionStat
from rest_framework import serializers

from eve_db.models.chr import *
from eve_db.models.inventory import *
from eve_db.models.map import *
from eve_db.models.npc import *
from eve_db.models.planet import *
from eve_db.models.station import *
from eve_db.models.system import *


#
# market_data serializers
#


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        exclude = ('uploader_ip_hash', 'message_key')


class ItemRegionStatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemRegionStat


class OrderHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderHistory

#
# eve_db serializers
#


# Character

class ChrRaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChrRace


class ChrBloodlineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChrBloodline


class ChrAncestrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChrAncestry


class ChrFactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChrFaction


# Inventory

class InvNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvName


class InvMarketGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvMarketGroup


class InvCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvCategory


class InvGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvGroup


class InvMetaGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvMetaGroup


class InvTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvType


class InvTypeMaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvTypeMaterial


class InvMetaTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvMetaType


class InvFlagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvFlag


class DgmAttributeCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DgmAttributeCategory


class DgmAttributeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DgmAttributeType


class DgmTypeAttributeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DgmTypeAttribute


class DgmEffectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DgmEffect


class DgmTypeEffectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DgmTypeEffect


class InvPOSResourcePurposeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvPOSResourcePurpose


class InvPOSResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvPOSResource


class InvTypeReactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvTypeReaction


class InvContrabandTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvContrabandType


class InvItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvItem


class InvPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvPosition


class InvUniqueNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvUniqueName



# Map


class MapUniverseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapUniverse


class MapRegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapRegion


class MapRegionJumpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapRegionJump


class MapConstellationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapConstellation


class MapConstellationJumpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapConstellationJump


class MapSolarSystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapSolarSystem


class MapSolarSystemJumpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapSolarSystemJump


class MapJumpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapJump


class MapCelestialStatisticSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapCelestialStatistic


class MapDenormalizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapDenormalize


class MapLandmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapLandmark


class MapLocationSceneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapLocationScene


class MapLocationWormholeClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapLocationWormholeClass


class WarCombatZoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WarCombatZone


class WarCombatZoneSystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WarCombatZoneSystem


# NPC


class CrpActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CrpActivity


class CrpNPCCorporationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CrpNPCCorporation


class CrpNPCDivisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CrpNPCDivision


class CrpNPCCorporationDivisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CrpNPCCorporationDivision


class CrpNPCCorporationTradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CrpNPCCorporationTrade


class CrpNPCCorporationResearchFieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CrpNPCCorporationResearchField


class AgtAgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgtAgent


class AgtAgentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgtAgentType


class AgtResearchAgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgtResearchAgent


# Planet


class PlanetSchematicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanetSchematic


class PlanetSchematicsPinMapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanetSchematicsPinMap


class PlanetSchematicsTypeMapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanetSchematicsTypeMap


# Station


class RamActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RamActivity

class RamAssemblyLineTypeDetailPerCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RamAssemblyLineTypeDetailPerCategory


class RamAssemblyLineTypeDetailPerGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RamAssemblyLineTypeDetailPerGroup


class RamAssemblyLineTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RamAssemblyLineType


class RamAssemblyLineStationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RamAssemblyLineStations


class StaServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaService


class StaStationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaStationType


class StaOperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaOperation


class StaStationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaStation


class StaOperationServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaOperationServices


class RamInstallationTypeContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RamInstallationTypeContent


# System

class EveUnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EveUnit
